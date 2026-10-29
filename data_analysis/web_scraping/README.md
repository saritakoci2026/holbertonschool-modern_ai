# Web Scraping

This project introduces web scraping using Python.

## Task 0: Fetch HTML

The `0-fetch_html.py` module contains the `fetch_html`
function, which retrieves HTML content from a URL using
the `requests` library.

The function supports optional HTTP headers and a timeout.
It raises an exception for HTTP error status codes and
returns the HTML response as text.

## Task 8: Scroll & Scrape Products

**File:** `8-scroll_and_scrape.py`

Scrapes infinite-scroll JS-rendered product pages using Selenium.

### Usage
```bash
./8-main.py