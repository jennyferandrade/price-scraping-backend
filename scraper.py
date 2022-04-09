import requests
import pandas as pd

HEADERS = (
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                      'Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

price_scraping_source = pd.read_csv('products.csv', sep=';')
prod_tracker_URLS = price_scraping_source.url
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)
print(page)