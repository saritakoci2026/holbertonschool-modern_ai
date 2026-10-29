#!/usr/bin/env python3
"""Test the static product scraping function."""

scrape_products = __import__(
    '6-products_list'
).scrape_products_list

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

try:
    products = scrape_products(url)

    for i, product in enumerate(products):
        print(f"Product #{i}:")
        print(product)
except Exception as error:
    print(str(error))
