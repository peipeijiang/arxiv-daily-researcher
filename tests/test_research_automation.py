import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from enrichers.github_code import GitHubCodeEnricher
from library.feedback import FeedbackStore
from library.research_library import ResearchLibrary
from sources.base_source import PaperMetadata
from sync_feedback import parse_feedback


class ResearchAutomationTests(unittest.TestCase):
    def test_feedback_parser_uses_latest_action(self):
        result = parse_feedback(
            [
                {"number": 1, "title": "[LIKE] arxiv:1"},
                {"number": 2, "title": "[IGNORE] arxiv:1"},
            ]
        )
        self.assertEqual(result, {"liked": [], "ignored": ["arxiv:1"]})

    def test_feedback_store_boosts_liked_paper(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "feedback.json"
            path.write_text('{"liked":["p1"],"ignored":[]}', encoding="utf-8")
            score = SimpleNamespace(total_score=70.0, reasoning="base", is_qualified=False)
            FeedbackStore(path).apply("p1", score)
            self.assertEqual(score.total_score, 80.0)
            self.assertTrue(score.is_qualified)

    def test_github_enricher_filters_unrelated_results(self):
        enricher = GitHubCodeEnricher(token="test")
        response = Mock()
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "items": [
                {
                    "name": "modern-recommender-models",
                    "full_name": "lab/modern-recommender-models",
                    "description": "Modern recommender models with graph learning",
                    "html_url": "https://github.com/lab/modern-recommender-models",
                    "stargazers_count": 42,
                    "updated_at": "2026-01-01T00:00:00Z",
                },
                {"name": "unrelated", "description": "image editor"},
            ]
        }
        enricher.session.get = Mock(return_value=response)
        matches = enricher.find("Modern Recommender Models with Graph Learning")
        self.assertEqual([item["full_name"] for item in matches], ["lab/modern-recommender-models"])

    def test_library_deduplicates_index_and_writes_graph(self):
        with tempfile.TemporaryDirectory() as tmp:
            paper = PaperMetadata(
                paper_id="arxiv:1",
                source="arxiv",
                title="A Recommender Paper",
                authors=["A. Author"],
                abstract="Abstract",
                url="https://example.com/paper",
                published_date=datetime(2026, 7, 12),
                openalex_id="W1",
                referenced_works=["W2"],
                related_works=["W3"],
            )
            score = SimpleNamespace(total_score=88.0, is_qualified=True, tldr="Useful")
            rows = {"arxiv": [{"paper_metadata": paper, "score_response": score, "abstract_cn": "摘要"}]}
            library = ResearchLibrary(Path(tmp) / "knowledge")
            library.persist(rows, {})
            library.persist(rows, {})
            self.assertEqual(len(library.index_path.read_text().splitlines()), 1)
            graph = json.loads(library.graph_path.read_text())
            self.assertEqual({edge["type"] for edge in graph["edges"]}, {"cites", "related"})


if __name__ == "__main__":
    unittest.main()
