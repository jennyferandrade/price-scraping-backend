class AmazonScraper:

    def __init__(self, html):
        self.html = html    # instance variable unique to each instance

    def search_product_title(self):
        return self.html.find(id='productTitle').get_text().strip()

    def search_product_price(self):
        try:
            # you will get the price like this "2.804,15€", so we are transforming to get something like this "2804.15"
            return float(
                self.html.select_one('.a-offscreen').get_text().replace('.', '').replace('€', '').replace(',', '.').strip()
            )
        except:
            return 'No price available'

    def search_product_availability(self):
        try:
            self.html.select('#availability .a-color-state')[0].get_text().strip()
            return 'Out of Stock'
        except:
            try:
                self.html.select('#availability .a-color-price')[0].get_text().strip()
                return 'Out of Stock'
            except:
                return 'Available'
