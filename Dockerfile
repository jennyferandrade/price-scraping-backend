FROM python:latest

WORKDIR /

COPY requirements.txt /
COPY price_history.csv /
COPY products.csv /
COPY amazon_scraper.py /
COPY scraper.py /

RUN pip install -r /requirements.txt

CMD [ "python", "scraper.py"]