#!/usr/bin/env python3
"""Scrape details from a single product page."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Open a product page and return its details."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element(
            "css selector", ".caption"
        )
        title_elements = caption.find_elements(
            "css selector", "h4"
        )
        price_element = driver.find_element(
            "css selector", "h4.price"
        )
        description_element = driver.find_element(
            "css selector", "p.description"
        )
        rating_elements = driver.find_elements(
            "css selector", ".ratings .ws-icon-star"
        )

        return {
            "title": title_elements[1].text,
            "price": price_element.text,
            "description": description_element.text,
            "rating": len(rating_elements)
        }

    finally:
        driver.quit()
