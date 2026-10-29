#!/usr/bin/env python3
"""Test the login and quote scraping function."""

login_and_scrape = __import__(
    '5-login_and_scrape'
).login_and_scrape

login_url = "https://quotes.toscrape.com/login"

try:
    quotes = login_and_scrape(
        login_url,
        user="foo",
        pwd="bar"
    )

    for i, quote in enumerate(quotes):
        print(f"Quote #{i}:")
        print(quote)
except Exception as error:
    print(str(error))
