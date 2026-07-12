#!/usr/bin/env python3
"""Build and optionally deliver a seven-day research synthesis."""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from config import settings


def recent_records(path=Path("knowledge/index.jsonl"), days=7):
    if not path.exists():
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    records = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
            updated = datetime.fromisoformat(row["updated_at"]).replace(tzinfo=timezone.utc)
            if updated >= cutoff and row.get("qualified"):
                records[row["paper_id"]] = row
        except (ValueError, KeyError, json.JSONDecodeError):
            continue
    return sorted(records.values(), key=lambda row: row.get("score", 0), reverse=True)


def main():
    records = recent_records()
    if not records:
        print("No qualified papers found for this week.")
        return
    compact = [
        {
            "title": row.get("title"),
            "source": row.get("source"),
            "score": row.get("score"),
            "tldr": row.get("tldr"),
            "topics": row.get("topics", [])[:5],
            "citations": row.get("cited_by_count", 0),
            "code": row.get("code_repositories", [])[:2],
            "url": row.get("url"),
        }
        for row in records[:50]
    ]
    prompt = """你是推荐系统研究负责人。基于下面最近七天论文，输出中文周报 Markdown。
必须包含：本周三大研究主题、方法与技术演进、证据与代表论文、可运行代码仓库、值得追踪的研究空白、下周阅读优先级。区分论文事实与推断，引用论文标题和链接，内容精炼但具体。\n\n"""
    client = OpenAI(api_key=settings.SMART_LLM.api_key, base_url=settings.SMART_LLM.base_url)
    response = client.chat.completions.create(
        model=settings.SMART_LLM.model_name,
        temperature=settings.SMART_LLM.temperature,
        messages=[{"role": "user", "content": prompt + json.dumps(compact, ensure_ascii=False)}],
    )
    content = response.choices[0].message.content
    now = datetime.now()
    path = Path("knowledge/reports/weekly") / f"{now:%Y}-W{now:%W}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# 推荐系统研究周报 {now:%Y-%m-%d}\n\n{content}\n", encoding="utf-8")

    webhook = os.getenv("WECHAT_WEBHOOK_URL", "")
    if webhook:
        repo_url = os.getenv("FEEDBACK_REPO_URL", "")
        report_url = f"{repo_url}/blob/main/{path}" if repo_url else ""
        summary = content[:3000]
        if report_url:
            summary += f"\n\n[查看完整周报]({report_url})"
        result = requests.post(webhook, json={"msgtype": "markdown", "markdown": {"content": summary}}, timeout=30)
        result.raise_for_status()
    print(f"Weekly digest written to {path}")


if __name__ == "__main__":
    main()
