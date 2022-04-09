import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

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

while True:
    for x, url in enumerate(product_urls):
        now = datetime.now().strftime('%Y-%m-%d %Hh%Mm')
        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.content, 'html.parser')
        scrapper = AmazonScraper(soup)
        log = pd.DataFrame({'date': now.replace('h', ':').replace('m', ''),
                            'code': price_scraping_source.code[x],
                            'url': url,
                            'title': scrapper.search_product_title(),
                            'higher_alert': price_scraping_source.higher_alert[x],
                            'lower_alert': price_scraping_source.lower_alert[x],
                            'price': scrapper.search_product_price(),
                            'stock': scrapper.search_product_availability(),
                            }, index=[x])
        price_scraping_log = pd.concat([price_scraping_log, log])

    price_scraping_log.to_csv('price_history.csv', mode='a', index=False, header=False)
    time.sleep(21600)
