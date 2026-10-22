#!/usr/bin/env python3
"""Scrape quotes from the Quotes to Scrape API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Return quotes collected from all API pages."""
    all_quotes = []
    page = 1

    while True:
        url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        response = fetch_html(url)

        if not response:
            break

        try:
            data = json.loads(response)
        except (json.JSONDecodeError, TypeError):
            break

        quotes = data.get("quotes", [])
        if not quotes:
            break

        for quote in quotes:
            author = quote.get("author", {})
            if isinstance(author, dict):
                author = author.get("name", "")

            all_quotes.append({
                "text": quote.get("text", ""),
                "author": author,
                "tags": quote.get("tags", [])
            })

        if not data.get("has_next", False):
            break

        page += 1

    return all_quotes
