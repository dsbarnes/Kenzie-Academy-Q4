import requests
from portfolio.models import Company

# add secret api keys
import os
from dotenv import load_dotenv
from Stocker.settings import BASE_DIR
load_dotenv(dotenv_path=f'{BASE_DIR}/Stocker/.env')

def fetchCompanyData(ticker):
    key = os.getenv("IEX_KEY_1")
    ticker = ticker.upper()
    r = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/company?token={key}')
    return r.json()


def fetchTicker(ticker):
    key = os.getenv("IEX_KEY_2")
    ticker = ticker.upper()
    r = requests.get(f'https://sandbox.iexapis.com/stable/stock/{ticker}/quote?token={key}')

    co = Company.objects.filter(ticker_symbol=ticker).first()
    if co:
        co.price = r.json()['latestPrice']
        co.save()
    else:
        Company.objects.create(name=r.json()['companyName'],
                               ticker_symbol=r.json()['symbol'],
                               price=r.json()['latestPrice'])

    return r.json()


def multiFetcher(follow_list):
    stock_tickers = []
    for tkr in follow_list:
        data = fetchTicker(tkr)
        stock_tickers.append({
            'symbol': tkr,
            'company': data['companyName'],
            'price': data['latestPrice'],
            'change': data['change']
        })

    return stock_tickers