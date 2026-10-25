#!/usr/bin/env python3
"""Scroll through a page and scrape unique products."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through an infinite-scroll page and scrape products."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()

    try:
        driver.get(url)

        previous_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(scroll_pause)

            current_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if current_height <= previous_height:
                break

            previous_height = current_height

        cards = driver.find_elements(
            By.CSS_SELECTOR, "div.thumbnail"
        )

        for card in cards:
            title_elements = card.find_elements(
                By.CSS_SELECTOR, "a.title"
            )
            price_elements = card.find_elements(
                By.CSS_SELECTOR, "h4.price"
            )
            description_elements = card.find_elements(
                By.CSS_SELECTOR, "p.description"
            )
            rating_elements = card.find_elements(
                By.CSS_SELECTOR, ".ratings .ws-icon-star"
            )

            if not title_elements or not price_elements:
                continue

            title = title_elements[0].get_attribute("title")
            price = price_elements[0].text.strip()

            description = ""
            if description_elements:
                description = description_elements[0].text.strip()

            key = (title, price)

            if key in seen:
                continue

            seen.add(key)

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": len(rating_elements)
            })

    finally:
        driver.quit()

    return products
