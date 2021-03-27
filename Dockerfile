FROM python:latest
RUN pip install parsel requests
RUN mkdir btc_scrape
COPY . .
WORKDIR /btc_scrape/src
