import requests
from bs4 import BeautifulSoup
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
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text().strip()
try:
    # you will get the price like this "2.804,15€", so we are transforming to get something like this "2804.15"
    price = float(
        soup.select_one('.a-offscreen').get_text().replace('.', '').replace('€', '').replace(',', '.').strip()
    )
except:
    price = ''


try:
    soup.select('#availability .a-color-state')[0].get_text().strip()
    stock = 'Out of Stock'
except:
    try:
        soup.select('#availability .a-color-price')[0].get_text().strip()
        stock = 'Out of Stock'
    except:
        stock = 'Available'

print(title + " " + str(price) + " " + stock)
