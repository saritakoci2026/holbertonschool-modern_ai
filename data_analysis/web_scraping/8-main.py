#!/usr/bin/env python3
"""Test the infinite-scroll product scraper."""

scroll_and_scrape = __import__(
    '8-scroll_and_scrape'
).scroll_and_scrape

url = (
    "https://webscraper.io/test-sites/e-commerce/"
    "scroll/computers/laptops"
)

try:
    products = scroll_and_scrape(url)

    print(f"Total products: {len(products)}")

    for i, product in enumerate(products):
        print(f"Product #{i}:")
        print(product)

except Exception as error:
    print(f"Error: {error}")
