#!/usr/bin/env python3
"""
Collect accessible paper/poster corpus evidence from official conference virtual pages.

This script is intentionally lightweight:
- it counts poster links from official index pages,
- optionally samples a handful of poster pages,
- and writes a JSON summary for poster-skill refresh work.

It is not meant to crawl the whole corpus every time a poster is drafted.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin

import requests


DEFAULT_SOURCES = [
    {
        "venue": "NeurIPS",
        "year": 2024,
        "index_url": "https://nips.cc/virtual/2024/papers.html?filter=titles",
        "sample_urls": [
            "https://nips.cc/virtual/2024/poster/92923",
            "https://nips.cc/virtual/2024/poster/92924",
            "https://nips.cc/virtual/2024/poster/92925",
        ],
    },
    {
        "venue": "NeurIPS",
        "year": 2023,
        "index_url": "https://nips.cc/virtual/2023/papers.html?filter=titles",
        "sample_urls": [
            "https://nips.cc/virtual/2023/poster/69865",
            "https://nips.cc/virtual/2023/poster/69866",
            "https://nips.cc/virtual/2023/poster/69867",
        ],
    },
    {
        "venue": "ICLR",
        "year": 2024,
        "index_url": "https://iclr.cc/virtual/2024/papers.html?filter=titles",
        "sample_urls": [
            "https://iclr.cc/virtual/2024/poster/17365",
            "https://iclr.cc/virtual/2024/poster/17366",
            "https://iclr.cc/virtual/2024/poster/17367",
        ],
    },
    {
        "venue": "CVPR",
        "year": 2024,
        "index_url": "https://cvpr.thecvf.com/virtual/2024/papers.html?filter=titles",
        "sample_urls": [
            "https://cvpr.thecvf.com/virtual/2024/poster/29177",
            "https://cvpr.thecvf.com/virtual/2024/poster/29178",
            "https://cvpr.thecvf.com/virtual/2024/poster/29179",
        ],
    },
]


@dataclass
class SourceSummary:
    venue: str
    year: int
    index_url: str
    poster_links: int
    sample_urls: list[str]
    sample_titles: list[str]
    poster_urls: list[str] | None = None


def fetch_text(url: str, timeout: int) -> str:
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def count_poster_links(html: str) -> int:
    return len(set(re.findall(r"/virtual/\d{4}/poster/\d+", html)))


def extract_poster_urls(index_url: str, html: str) -> list[str]:
    links = sorted(set(re.findall(r"/virtual/\d{4}/poster/\d+", html)))
    return [urljoin(index_url, link) for link in links]


def extract_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.S | re.I)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def iter_sources(venues: Iterable[str] | None) -> list[dict]:
    if not venues:
        return DEFAULT_SOURCES
    wanted = {v.lower() for v in venues}
    return [src for src in DEFAULT_SOURCES if src["venue"].lower() in wanted]


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect paper/poster corpus evidence.")
    parser.add_argument(
        "--venue",
        action="append",
        help="Limit to one or more venues, e.g. --venue NeurIPS --venue CVPR",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds.",
    )
    parser.add_argument(
        "--output",
        default="references/poster-corpus-scan.json",
        help="Output JSON path relative to cwd.",
    )
    parser.add_argument(
        "--include-links",
        action="store_true",
        help="Include every extracted poster URL in the output JSON.",
    )
    args = parser.parse_args()

    summaries: list[SourceSummary] = []
    total_links = 0

    for source in iter_sources(args.venue):
        html = fetch_text(source["index_url"], args.timeout)
        poster_urls = extract_poster_urls(source["index_url"], html)
        poster_links = len(poster_urls)
        total_links += poster_links

        sample_titles: list[str] = []
        for sample_url in source["sample_urls"]:
            try:
                sample_html = fetch_text(sample_url, args.timeout)
                sample_titles.append(extract_title(sample_html))
            except Exception as exc:  # pragma: no cover - network dependent
                sample_titles.append(f"ERROR: {exc}")

        summaries.append(
            SourceSummary(
                venue=source["venue"],
                year=source["year"],
                index_url=source["index_url"],
                poster_links=poster_links,
                sample_urls=source["sample_urls"],
                sample_titles=sample_titles,
                poster_urls=poster_urls if args.include_links else None,
            )
        )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_poster_links": total_links,
        "sources": [asdict(item) for item in summaries],
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
