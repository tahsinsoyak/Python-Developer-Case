from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
import time

def scrape_trendyol(url):
    # Set the path to your driver executable (replace 'chromedriver.exe' with the correct path)
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(url)
    time.sleep(2)

    # Find the "product-listing-container" element
    product_listing_container = driver.find_element(By.XPATH, '//*[@id="category-top-ranking"]/div/div[3]/div')
    time.sleep(2)

    # Find all product cards within the container
    product_cards = product_listing_container.find_elements(By.XPATH, '//div[@class="product-card"]')

    product_data = []

    # Loop through each product card and extract data
    for product_card in product_cards:
        # Extract data from each product card
        product_brand = product_card.find_element(By.XPATH, './/span[@class="product-brand"]').text
        product_name = product_card.find_element(By.XPATH, './/span[@class="product-name"]').text
        product_price = product_card.find_element(By.XPATH, './/div[@class="prc-box-dscntd"]').text
        product_image = product_card.find_element(By.XPATH, './/img[@class="product-img"]').get_attribute('src')
        product_link = product_card.find_element(By.XPATH, './/a').get_attribute('href')
        time.sleep(2)

        # Print or store the extracted data
        print(f"Product Brand: {product_brand}")
        print(f"Product Name: {product_name}")
        print(f"Product Discount: {product_price}")
        print(f"Product Image: {product_image}")
        print(f"Product Link: {product_link}")
        print("")

        product_info = {
            'Brand': product_brand,
            'Name': product_name,
            'Price': product_price,
            'Image': product_image,
            'Link': product_link
        }

        # Append the product info to the list
        product_data.append(product_info)

    # Close the web driver
    driver.quit()

    return product_data

# List of URLs to scrape
urls_to_scrape = [
    'https://www.trendyol.com/cok-satanlar?categoryId=33&type=mostFavourite&webGenderId=1',
    'https://www.trendyol.com/cok-satanlar?categoryId=33&type=mostRated&webGenderId=1',
    'https://www.trendyol.com/cok-satanlar?categoryId=33&type=topViewed&webGenderId=1'
]

# Loop through the URLs and scrape data
for url in urls_to_scrape:
    scraped_data = scrape_trendyol(url)
    # You can do further processing with the scraped data as needed
