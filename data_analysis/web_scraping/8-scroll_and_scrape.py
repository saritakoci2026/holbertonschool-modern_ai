#!/usr/bin/env python3
"""Scrape products from an infinite-scroll web page."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through a page and return a list of unique products."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        unchanged_count = 0
        previous_count = 0
        max_scrolls = 100

        for _ in range(max_scrolls):
            cards = driver.find_elements(
                By.CSS_SELECTOR, "div.thumbnail"
            )
            current_count = len(cards)

            if current_count > previous_count:
                unchanged_count = 0
                previous_count = current_count
            else:
                unchanged_count += 1

            if unchanged_count >= 4:
                break

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(scroll_pause)

        cards = driver.find_elements(
            By.CSS_SELECTOR, "div.thumbnail"
        )

        for card in cards:
            try:
                title_element = card.find_element(
                    By.CSS_SELECTOR, "a.title"
                )
                price_element = card.find_element(
                    By.CSS_SELECTOR, "h4.price"
                )
                description_element = card.find_element(
                    By.CSS_SELECTOR, "p.description"
                )

                title = title_element.get_attribute("title")
                price = price_element.text
                description = description_element.text

                product_key = (title, price)

                if product_key in seen:
                    continue

                seen.add(product_key)

                rating_elements = card.find_elements(
                    By.CSS_SELECTOR,
                    ".ratings .glyphicon-star, "
                    ".ratings .ws-icon-star, "
                    ".ratings span.glyphicon-star"
                )

                products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": len(rating_elements)
                })

            except Exception:
                continue

    finally:
        driver.quit()

    return products
