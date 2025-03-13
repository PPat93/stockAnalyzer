"""
API data retriever component:
Sends data to Integrator -> Analyzer;
Sends API request to retrieve needed values;
Receives response with retrieved values;
Extract values from the response and deletes everything that is not needed;
"""

import os
import requests

FUNDAMENTAL_API_KEY = os.environ.get("fundamentalRetrieverApiKey")
PRICE_API_KEY = os.environ.get("realtimeRetrieverApiKey")
HEADERS = {"Content-Type": "application/json"}


class StockRetriever:
    """Class for stock data retrieving"""

    def __init__(self, ticker) -> object:
        self.ticker = ticker

    # shared with crypto price - max 50 reqs/hour, 1000 reqs/day
    def retrieve_last_stock_price(self):
        """Retrieve latest stock price"""
        price_api_uri = (
            f"https://api.tiingo.com/iex/{self.ticker}?token={PRICE_API_KEY}"
        )

        price_res = requests.get(price_api_uri, headers=HEADERS, timeout=10)
        price_json = price_res.json()

        # tngoLast - shortly, this is a property that holds latest or mid value of the stock,
        # depending on external factors
        return price_json[0].get("tngoLast")

    # max 25 reqs/day
    def retrieve_stock_fundamental_data(self):
        """Retrieve fundamental data for the specified stock"""
        fundamental_api_uri = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.ticker}&apikey={FUNDAMENTAL_API_KEY}"

        fundamental_res = requests.get(fundamental_api_uri, headers=HEADERS, timeout=10)
        fundamental_json = fundamental_res.json()

        return fundamental_json


class CryptoRetriever:
    """Class for crypto data retrieving"""

    def __init__(self, ticker: str) -> object:
        self.ticker = ticker

    # shared with stock price - max 50 reqs/hour, 1000 reqs/day
    def retrieve_last_crypto_price(self):
        """Retrieve latest crypto price"""
        crypto_api_uri = f"https://api.tiingo.com/tiingo/crypto/top?tickers={self.ticker}&token={PRICE_API_KEY}"

        crypto_res = requests.get(crypto_api_uri, headers=HEADERS, timeout=10)
        crypto_json = crypto_res.json()

        return crypto_json