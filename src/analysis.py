from scrapper import scrape

def btc_can_rises():
    bitcoin_max_market_cap = 21000000
    bitcoin_supply = 18665937
    global_market_cap = sum(scrape()) - bitcoin_supply
    total = str(global_market_cap / bitcoin_max_market_cap)
    print("The price of Bitcoin needs to rise "+total+" times yet")