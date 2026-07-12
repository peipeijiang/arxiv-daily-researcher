"""Find likely official code repositories for research papers."""

import os
import re
from typing import Dict, List

import requests


class GitHubCodeEnricher:
    API_URL = "https://api.github.com/search/repositories"

    def __init__(self, token: str = None):
        self.session = requests.Session()
        token = token or os.getenv("GITHUB_TOKEN", "")
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        self.session.headers.update(
            {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        )

    @staticmethod
    def _tokens(title: str) -> set:
        return {
            token
            for token in re.findall(r"[a-z0-9]+", title.lower())
            if len(token) >= 4 and token not in {"with", "from", "using", "based", "towards"}
        }

    def find(self, title: str, max_results: int = 3) -> List[Dict]:
        query = f'"{title[:180]}" in:readme'
        try:
            response = self.session.get(
                self.API_URL,
                params={"q": query, "sort": "stars", "order": "desc", "per_page": 10},
                timeout=20,
            )
            if response.status_code in (403, 429):
                return []
            response.raise_for_status()
        except requests.RequestException:
            return []

        title_tokens = self._tokens(title)
        matches = []
        for item in response.json().get("items", []):
            text = f"{item.get('name', '')} {item.get('description') or ''}"
            overlap = len(title_tokens & self._tokens(text))
            if title_tokens and overlap / len(title_tokens) < 0.15:
                continue
            matches.append(
                {
                    "full_name": item.get("full_name"),
                    "url": item.get("html_url"),
                    "description": item.get("description"),
                    "stars": int(item.get("stargazers_count") or 0),
                    "updated_at": item.get("updated_at"),
                    "match": "readme-title",
                }
            )
            if len(matches) >= max_results:
                break
        return matches
