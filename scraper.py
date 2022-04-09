import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

from amazon_scraper import AmazonScraper

HEADERS = (
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                      'Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

price_scraping_source = pd.read_csv('products.csv', sep=';')
product_urls = price_scraping_source.url
price_scraping_log = pd.DataFrame()
now = datetime.now().strftime('%Y-%m-%d %Hh%Mm')

for x, url in enumerate(product_urls):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    scrapper = AmazonScraper(soup)
    print("Item" + str(x) + ": " + scrapper.search_product_title() + " " + str(scrapper.search_product_price()) + " " + scrapper.search_product_availability())
