#!/usr/bin/env python3
"""Scrape product information from a static e-commerce page."""

import time
from selenium import webdriver


def scrape_products(url):
    """Open a product page and return a list of product dictionaries."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    products = []

    try:
        driver.get(url)
        time.sleep(2)

        product_cards = driver.find_elements(
            "css selector", ".thumbnail"
        )

        for card in product_cards:
            title_element = card.find_element(
                "css selector", "a.title"
            )
            price_element = card.find_element(
                "css selector", "h4.price"
            )
            description_element = card.find_element(
                "css selector", "p.description"
            )
            rating_element = card.find_element(
                "css selector", ".ratings p[data-rating]"
            )

            product = {
                "title": title_element.get_attribute("title"),
                "price": price_element.text,
                "description": description_element.text,
                "rating": int(
                    rating_element.get_attribute("data-rating")
                )
            }

            products.append(product)

    finally:
        driver.quit()

    return products


def scrape_products_list(url):
    """Return products from a static product category page."""
    return scrape_products(url)
