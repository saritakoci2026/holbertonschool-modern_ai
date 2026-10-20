#!/usr/bin/env python3
"""Scrape quotes, authors, and tags from a static quotes page."""

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape quotes, authors, and tags from the first page."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    quotes_data = []

    quote_blocks = soup.select('div.quote')

    for quote in quote_blocks:
        text_element = quote.select_one('span.text')
        author_element = quote.select_one('small.author')
        tag_elements = quote.select('div.tags a.tag')

        if text_element is None or author_element is None:
            continue

        quote_data = {
            'text': text_element.get_text(strip=True),
            'author': author_element.get_text(strip=True),
            'tags': [
                tag.get_text(strip=True)
                for tag in tag_elements
            ],
        }

        quotes_data.append(quote_data)

    return quotes_data
