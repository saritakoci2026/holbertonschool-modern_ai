#!/usr/bin/env python3
"""Extract quotes from JSON-LD data embedded in a web page."""

import json

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Return quotes extracted from JSON-LD scripts at the given URL."""
    html = fetch_html(url)
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for script in soup.find_all(
        "script", type="application/ld+json"
    ):
        try:
            data = json.loads(script.string or script.get_text())
        except (json.JSONDecodeError, TypeError):
            continue

        objects = data if isinstance(data, list) else [data]

        for item in objects:
            if not isinstance(item, dict):
                continue

            if item.get("@type") != "Quote":
                continue

            author = item.get("author", {})
            if isinstance(author, dict):
                author = author.get("name")

            tags = item.get("keywords", [])
            if isinstance(tags, str):
                tags = [
                    tag.strip()
                    for tag in tags.split(",")
                    if tag.strip()
                ]

            quotes.append({
                "text": item.get("text"),
                "author": author,
                "tags": tags
            })

    return quotes
