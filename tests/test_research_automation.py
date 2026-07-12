import json
import os
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
from enrichers.open_access import OpenAccessResolver
from library.feedback import FeedbackStore
from library.research_library import ResearchLibrary
from library.evidence_builder import build_evidence_pack, audit_weekly_digest
from sources.base_source import PaperMetadata
from sources.citation_discovery import CitationDiscovery
from sync_feedback import parse_feedback
from notifications.notifier import NotifierAgent, WebhookNotifier


class ResearchAutomationTests(unittest.TestCase):
    def test_wechat_paper_card_uses_deep_analysis(self):
        agent = NotifierAgent.__new__(NotifierAgent)
        with unittest.mock.patch.dict(
            os.environ, {"FEEDBACK_REPO_URL": "https://github.com/o/r"}
        ):
            card = agent._format_wechat_paper_card(
                {
                    "paper_id": "arxiv:1",
                    "title": "An English Paper",
                    "source": "arxiv",
                    "score": 88,
                    "url": "https://arxiv.org/abs/1",
                    "tldr": "short",
                    "analysis": {
                        "_analysis_basis": "full_text",
                        "chinese_title": "一篇论文",
                        "summary": "完整核心结论",
                        "methodology": "完整方法",
                        "key_results": ["关键结果"],
                        "limitations": ["主要局限"],
                    },
                    "code_repositories": [],
                },
                1,
                5,
            )
        self.assertIn("全文深读", card)
        self.assertIn("完整方法", card)
        self.assertIn("关键结果", card)
        self.assertIn("主要局限", card)
        self.assertLessEqual(len(card.encode("utf-8")), 4000)

    def test_unpaywall_returns_repository_pdf_with_provenance(self):
        resolver = OpenAccessResolver(email="researcher@example.com")
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "best_oa_location": {
                "url_for_pdf": "https://repository.example.edu/paper.pdf",
                "host_type": "repository",
                "license": "cc-by",
                "version": "acceptedVersion",
            },
            "oa_locations": [],
        }
        resolver.session.get = Mock(return_value=response)
        result = resolver.from_unpaywall("https://doi.org/10.1/example")
        self.assertEqual(result["provider"], "unpaywall")
        self.assertEqual(result["license"], "cc-by")

    def test_openalex_repository_page_can_reveal_pdf(self):
        resolver = OpenAccessResolver()
        resolver._pdf_from_public_page = Mock(
            return_value="https://university.example.edu/files/paper.pdf"
        )
        paper = SimpleNamespace(
            open_access_candidates=[{
                "landing_page_url": "https://university.example.edu/item/1",
                "pdf_url": None,
                "source": "University Repository",
                "source_type": "repository",
                "license": None,
            }]
        )
        result = resolver.from_openalex_locations(paper)
        self.assertEqual(result["provider"], "institutional_or_author_repository")
    def test_wechat_truncation_never_cuts_markdown_link(self):
        link = "[忽略](https://github.com/example/issues/new?title=paper)\n"
        content = "标题\n" + link + ("普通内容\n" * 300)
        result = WebhookNotifier._truncate_wechat_markdown(content, max_bytes=500)
        self.assertLessEqual(len(result.encode("utf-8")), 500)
        self.assertIn(link.strip(), result)
        self.assertNotIn("https://github.com/example/issues/new?title=paper\n普通内容\n...", result)

    def test_feedback_links_omit_large_issue_body(self):
        with unittest.mock.patch.dict(os.environ, {"FEEDBACK_REPO_URL": "https://github.com/o/r"}):
            links = NotifierAgent._feedback_links(
                {"paper_id": "doi:10.1/example", "title": "A" * 500, "url": "https://example.com"}
            )
        self.assertNotIn("body=", links)
        self.assertIn("[喜欢]", links)
        self.assertIn("[忽略]", links)
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
        readme = Mock()
        readme.status_code = 200
        readme.raise_for_status.return_value = None
        import base64
        readme.json.return_value = {
            "content": base64.b64encode(b"Modern Recommender Models with Graph Learning").decode()
        }
        enricher.session.get = Mock(side_effect=[response, readme])
        matches = enricher.find("Modern Recommender Models with Graph Learning")
        self.assertEqual([item["full_name"] for item in matches], ["lab/modern-recommender-models"])
        self.assertEqual(matches[0]["classification"], "possible")
        self.assertTrue(matches[0]["evidence"])

    def test_declared_repository_is_official(self):
        enricher = GitHubCodeEnricher(token="test")
        search = Mock(status_code=200)
        search.raise_for_status.return_value = None
        search.json.return_value = {"items": []}
        repo = Mock()
        repo.raise_for_status.return_value = None
        repo.json.return_value = {
            "name": "paper-code",
            "full_name": "author/paper-code",
            "html_url": "https://github.com/author/paper-code",
            "description": "code",
            "owner": {"login": "author"},
            "stargazers_count": 1,
        }
        readme = Mock(status_code=404)
        enricher.session.get = Mock(side_effect=[search, repo, readme])
        matches = enricher.find("Paper", abstract="Code: https://github.com/author/paper-code")
        self.assertEqual(matches[0]["classification"], "official")

    def test_bibliography_repository_is_rejected_without_authority_evidence(self):
        enricher = GitHubCodeEnricher(token="test")
        item = {
            "full_name": "community/paper-list",
            "description": "A collection of works and survey",
            "owner": {"login": "community"},
        }
        enricher._readme = Mock(return_value="Paper title DOI 10.1/example")
        result = enricher._verify(item, "Paper title", [], None, "10.1/example")
        self.assertEqual(result["classification"], "rejected")
        self.assertEqual(result["confidence"], 0)

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

    def test_citation_discovery_is_bounded_and_records_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "index.jsonl"
            seed = {
                "paper_id": "seed", "title": "Seed", "score": 90, "qualified": True,
                "openalex_id": "W1", "related_works": ["W2"], "referenced_works": []
            }
            index.write_text(json.dumps(seed) + "\n")
            candidate = PaperMetadata(
                paper_id="candidate", source="citation", title="Candidate", authors=[], abstract="",
                published_date=datetime(2026, 7, 12), url="https://openalex.org/W2", openalex_id="W2"
            )
            openalex = Mock()
            openalex.lookup_by_ids.side_effect = lambda ids: {"W2": candidate} if ids else {}
            openalex.find_recent_citing.return_value = []
            openalex.is_processed.return_value = False
            result = CitationDiscovery(openalex, index).discover(set(), max_total=1)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].discovery["relation"], "related_to_seed")

    def test_weekly_evidence_audit_requires_two_papers_for_observation(self):
        with tempfile.TemporaryDirectory() as tmp:
            records = [
                {"paper_id": "p1", "title": "One", "url": "u1", "tldr": "one", "qualified": True},
                {"paper_id": "p2", "title": "Two", "url": "u2", "tldr": "two", "qualified": True},
            ]
            pack = build_evidence_pack(records, Path(tmp))
            valid, errors = audit_weekly_digest("[跨论文观察] 趋势。[P01-C01][P02-C01]", pack)
            self.assertTrue(valid, errors)
            valid, _ = audit_weekly_digest("[跨论文观察] 趋势。[P01-C01]", pack)
            self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
