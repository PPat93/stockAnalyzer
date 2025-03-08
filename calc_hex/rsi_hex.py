"""
RSI hex:
Calculates The Relative Strength Index for a given stock ticker.
The given time intervals will be used to determine the range of calculations.
Window parameter defines how much the old data influences the new data. 
    - Scientificly: Specifies decay in terms of center of mass. 
    - The larger the window, the greater the influence of older data on newer data.
Worth using with other ratios - great with MACD.
Base calculations are given in the comment. However, the Ta-Lib library was used 
for the calculations.
"""

# talib installation:
# py.exe -3.12 -m pip install TA_Lib-0.4.29-cp312-cp312-win_amd64.whl

import talib
import pandas as pd
import yfinance as yf


# def calc_rsi(data, window=14, adjust=False):
#     delta = data["Close"].diff(1).dropna()
#     loss = delta.copy()
#     gains = delta.copy()

#     gains[gains < 0] = 0
#     loss[loss > 0] = 0

#     gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
#     loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

#     RS = gain_ewm / loss_ewm
#     RSI = 100 - 100 / (1 + RS)
#     return RSI


class RSI:
    """Class for RSI calculation and all utilities around it"""

    def __init__(self, ticker: str, start_date: str, end_date: str) -> object:
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def calc_rsi(self):
        """Retrieve specified stock data range and calculate its RSI"""

        data_res = yf.download(self.ticker, self.start_date, self.end_date)

        # New RSI calculation - to be implemented. Get rid of TaLib

        return 'data_res["RSI"]'