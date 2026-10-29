#!/usr/bin/env python3
"""
Module for scrolling an infinite-scroll page and scraping products.
"""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Scroll an infinite-scroll page and extract all unique products.

    Args:
        url (str): The URL of the infinite-scroll page.
        scroll_pause (float): Seconds to wait between each scroll.

    Returns:
        list: A list of dicts, each with keys:
              "title", "price", "description", "rating".
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(scroll_pause)

        # Scroll to the bottom until the page height stops growing
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Extract products
        products = []
        seen = set()
        cards = driver.find_elements("css selector", "div.thumbnail")
        for card in cards:
            try:
                title_el = card.find_element(
                    "css selector", "a.title")
                title = title_el.get_attribute("title")

                price_el = card.find_element(
                    "css selector", "h4.price")
                price = price_el.text

                desc_el = card.find_element(
                    "css selector", "p.description")
                description = desc_el.text

                rating_els = card.find_elements(
                    "css selector",
                    ".ratings .glyphicon-star, .ratings .ws-icon-star")
                rating = len(rating_els)

                key = (title, price)
                if key in seen:
                    continue
                seen.add(key)

                products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                })
            except Exception:
                continue

        return products
    finally:
        driver.quit()
