#!/usr/bin/env python3
"""Log in to a website and scrape quotes after authentication."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in using the supplied credentials and scrape the quotes."""
    session = requests.Session()

    response = session.get(login_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_input = soup.find("input", attrs={"name": "csrf_token"})
    csrf_token = csrf_input["value"]

    payload = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    response = session.post(
        login_url,
        data=payload,
        timeout=10
    )
    response.raise_for_status()

    quotes_url = "https://quotes.toscrape.com/"
    response = session.get(quotes_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text_element = quote.find("span", class_="text")
        author_element = quote.find("small", class_="author")

        tags = [
            tag.get_text(strip=True)
            for tag in quote.select(".tags a.tag")
        ]

        if text_element and author_element:
            quotes.append({
                "text": text_element.get_text(strip=True),
                "author": author_element.get_text(strip=True),
                "tags": tags
            })

    return quotes
