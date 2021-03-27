from parsel import Selector
import requests
from time import sleep

def fetch_content(url):
    try:
        response = requests.get(url, timeout=3)
    except:
        raise ValueError("Error request")
    else:
        if response.status_code != 200:
            raise ValueError("Error code {response.status_code}")
        sleep(0.5)
        return Selector(text=response.text)

def scrape():
    url = "https://www.fiatmarketcap.com/"
    data_list = []
    row_size = 7
    data_table = fetch_content(url).css("#currency-ranking tbody tr td::text").getall()
    counter = 0
    for row in data_table:
        if counter % row_size == 3:
            data_list.append(int(row.replace(" BTC", "").replace(",", "")))
        counter += 1
    return data_list
