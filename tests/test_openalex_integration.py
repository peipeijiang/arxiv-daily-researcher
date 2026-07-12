from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import Mock

from src.sources.base_source import PaperMetadata
from src.sources.openalex_source import OpenAlexSource
from src.sources.search_agent import SearchAgent
from src.sources.semantic_scholar_enricher import SemanticScholarEnricher


class OpenAlexMetadataTests(TestCase):
    def test_maps_conference_metadata(self):
        item = {
            "id": "https://openalex.org/W123",
            "doi": "https://doi.org/10.1145/example",
            "title": "A Sequential Recommendation Method",
            "publication_date": "2026-07-10",
            "authorships": [{"author": {"display_name": "Ada Example"}}],
            "abstract_inverted_index": {"Recommendation": [0], "method": [1]},
            "primary_location": {
                "landing_page_url": "https://doi.org/10.1145/example",
                "source": None,
                "raw_source_name": "Proceedings of ACM SIGIR",
                "raw_type": "proceedings-article",
            },
            "locations": [],
            "best_oa_location": None,
            "open_access": {"is_oa": False},
            "cited_by_count": 3,
            "type": "article",
            "topics": [{"display_name": "Recommender Systems"}],
        }

        with TemporaryDirectory() as directory:
            source = OpenAlexSource(history_dir=Path(directory))
            paper = source._metadata_from_item(item, source="openalex")

        self.assertIsNotNone(paper)
        self.assertEqual(paper.journal, "Proceedings of ACM SIGIR")
        self.assertEqual(paper.publication_type, "proceedings-article")
        self.assertEqual(paper.cited_by_count, 3)
        self.assertEqual(paper.abstract, "Recommendation method")

    def test_merges_openalex_record_into_arxiv_record(self):
        arxiv = PaperMetadata(
            paper_id="2607.12345",
            title="A Sequential Recommendation Method",
            authors=["Ada Example"],
            abstract="Abstract",
            published_date=datetime.now(timezone.utc),
            url="https://arxiv.org/abs/2607.12345",
            source="arxiv",
            pdf_url="https://arxiv.org/pdf/2607.12345.pdf",
        )
        openalex = PaperMetadata(
            paper_id="https://doi.org/10.1145/example",
            title="A Sequential Recommendation Method",
            authors=["Ada Example"],
            abstract="Abstract",
            published_date=datetime.now(timezone.utc),
            url="https://doi.org/10.1145/example",
            source="openalex",
            doi="https://doi.org/10.1145/example",
            journal="Proceedings of ACM SIGIR",
            openalex_id="W123",
            cited_by_count=3,
        )

        agent = SearchAgent.__new__(SearchAgent)
        results = agent._deduplicate_across_sources(
            {"arxiv": [arxiv], "openalex": [openalex]}
        )

        self.assertEqual(results["openalex"], [])
        self.assertEqual(arxiv.doi, "https://doi.org/10.1145/example")
        self.assertEqual(arxiv.journal, "Proceedings of ACM SIGIR")
        self.assertEqual(arxiv.openalex_id, "W123")
        self.assertEqual(arxiv.cited_by_count, 3)


class SemanticScholarBatchTests(TestCase):
    def test_maps_batch_response_by_doi(self):
        enricher = SemanticScholarEnricher()
        response = Mock()
        response.status_code = 200
        response.json.return_value = [
            {
                "paperId": "s2-paper",
                "url": "https://www.semanticscholar.org/paper/s2-paper",
                "venue": "SIGIR",
                "tldr": {"text": "A concise summary."},
                "citationCount": 9,
                "influentialCitationCount": 2,
                "publicationTypes": ["Conference"],
                "externalIds": {"ArXiv": "2607.12345"},
                "openAccessPdf": {"url": "https://example.test/paper.pdf"},
            }
        ]
        response.raise_for_status.return_value = None
        enricher.session.post = Mock(return_value=response)

        result = enricher.get_papers_info_batch(["https://doi.org/10.1145/example"])

        paper = result["10.1145/example"]
        self.assertEqual(paper["paper_id"], "s2-paper")
        self.assertEqual(paper["influential_citation_count"], 2)
        self.assertEqual(paper["arxiv_id"], "2607.12345")
        self.assertEqual(paper["pdf_url"], "https://example.test/paper.pdf")
