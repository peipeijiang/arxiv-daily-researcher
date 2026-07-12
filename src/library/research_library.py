"""Git-backed long-term paper library and citation graph."""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class ResearchLibrary:
    def __init__(self, root: Path = Path("knowledge")):
        self.root = root
        self.papers_dir = root / "papers"
        self.graph_path = root / "graph.json"
        self.index_path = root / "index.jsonl"
        self.papers_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _slug(paper_id: str) -> str:
        return re.sub(r"[^a-zA-Z0-9._-]+", "-", paper_id).strip("-")[:140]

    def persist(self, scored_by_source: Dict, analyses_by_source: Dict) -> int:
        analysis_map = {
            row["paper_id"]: row.get("analysis")
            for rows in analyses_by_source.values()
            for row in rows
        }
        records_by_id: Dict[str, Dict] = {}
        if self.index_path.exists():
            for line in self.index_path.read_text(encoding="utf-8").splitlines():
                try:
                    existing = json.loads(line)
                    records_by_id[existing["paper_id"]] = existing
                except (json.JSONDecodeError, KeyError):
                    continue
        graph = {"nodes": {}, "edges": []}
        if self.graph_path.exists():
            graph = json.loads(self.graph_path.read_text(encoding="utf-8"))

        for source, rows in scored_by_source.items():
            for row in rows:
                paper = row["paper_metadata"]
                score = row["score_response"]
                record = paper.to_dict()
                record.update(
                    {
                        "source": source,
                        "score": score.total_score,
                        "qualified": score.is_qualified,
                        "tldr": score.tldr,
                        "abstract_cn": row.get("abstract_cn", ""),
                        "analysis": analysis_map.get(paper.paper_id),
                        "updated_at": datetime.now().isoformat(),
                    }
                )
                slug = self._slug(paper.paper_id)
                path = self.papers_dir / f"{slug}.md"
                frontmatter = {
                    "title": paper.title,
                    "paper_id": paper.paper_id,
                    "source": source,
                    "published": record.get("published_date"),
                    "score": score.total_score,
                    "tags": ["paper", "recommender-systems"] + paper.topics[:5],
                }
                body = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in frontmatter.items()] + ["---", "", f"# {paper.title}", "", score.tldr, "", "## Metadata", "", f"- Authors: {', '.join(paper.authors)}", f"- DOI: {paper.doi or ''}", f"- URL: {paper.url}", f"- Venue: {paper.journal or source}", f"- Score: {score.total_score:.1f}", "", "## Abstract", "", paper.abstract, "", "## Chinese Abstract", "", row.get("abstract_cn", "")]
                if paper.code_repositories:
                    body += ["", "## Code", ""] + [f"- [{repo['full_name']}]({repo['url']}) - {repo['stars']} stars" for repo in paper.code_repositories]
                if record.get("analysis"):
                    body += ["", "## Deep Analysis", "", "```json", json.dumps(record["analysis"], ensure_ascii=False, default=str, indent=2), "```"]
                path.write_text("\n".join(body) + "\n", encoding="utf-8")
                records_by_id[paper.paper_id] = record
                graph["nodes"][paper.openalex_id or paper.paper_id] = {"title": paper.title, "paper_id": paper.paper_id}
                source_id = paper.openalex_id or paper.paper_id
                graph["edges"] = [edge for edge in graph["edges"] if edge.get("from") != source_id]
                graph["edges"] += [{"from": source_id, "to": target, "type": "cites"} for target in paper.referenced_works]
                graph["edges"] += [{"from": source_id, "to": target, "type": "related"} for target in paper.related_works]

        with self.index_path.open("w", encoding="utf-8") as handle:
            for record in sorted(records_by_id.values(), key=lambda item: item.get("updated_at", "")):
                handle.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
        self.graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
        return sum(len(rows) for rows in scored_by_source.values())
