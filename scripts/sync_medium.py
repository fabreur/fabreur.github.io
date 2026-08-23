#!/usr/bin/env python3
"""Fetch Fabio Reis' Medium RSS feed and write Jekyll data."""

from __future__ import annotations

import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

FEED_URL = "https://medium.com/feed/@fabreur"
OUTPUT = Path(__file__).resolve().parents[1] / "_data" / "medium.json"


def plain_text(value: str | None) -> str:
    text = re.sub(r"<[^>]+>", "", value or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main() -> None:
    request = urllib.request.Request(FEED_URL, headers={"User-Agent": "FabioReisBlog/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("Medium RSS feed has no channel")

    posts = []
    for item in channel.findall("item")[:10]:
        published = item.findtext("pubDate") or ""
        try:
            published = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=timezone.utc).isoformat()
        except ValueError:
            pass
        posts.append(
            {
                "title": plain_text(item.findtext("title")),
                "url": plain_text(item.findtext("link")),
                "date": published,
                "description": plain_text(item.findtext("description"))[:220],
                "categories": [plain_text(category.text) for category in item.findall("category") if plain_text(category.text)],
            }
        )

    OUTPUT.write_text(json.dumps({"updated_at": datetime.now(timezone.utc).isoformat(), "posts": posts}, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
