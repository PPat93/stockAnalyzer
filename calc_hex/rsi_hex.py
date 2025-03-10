"""
RSI:
Calculates The Relative Strength Index for a given stock ticker.
The given time intervals will be used to determine the range of calculations.
Window parameter defines how much the old data influences the new data. 
    - Scientifically: Specifies decay in terms of center of mass.
    - The larger the window, the greater the influence of older data on newer data.
Worth using with other ratios - great with MACD.
Base calculations are given in the comment.
"""

import yfinance as yf
import utils.utils as ut


class RSI:
    """Class for RSI calculation and all utilities around it"""

    def __init__(self, ticker: str, start_date: str, end_date: str, **kwargs):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.adjust = kwargs.get('adjust', False)
        self.window = kwargs.get('window', 14)
        self.market = kwargs.get('market', 'XETR')

    def calc_rsi(self):
        """Retrieve specified stock data range and calculate its RSI"""

        data_res = yf.download(self.ticker, self.start_date, self.end_date)
        window = ut.calculate_window(self.start_date, self.end_date, self.market)
        delta = data_res["Close"].diff(1).dropna()
        loss = delta.copy()
        gains = delta.copy()

        gains[gains < 0] = 0
        loss[loss > 0] = 0

        gain_ewm = gains.ewm(com=window - 1, adjust=self.adjust).mean()
        loss_ewm = abs(loss.ewm(com=window - 1, adjust=self.adjust).mean())

        RS = gain_ewm / loss_ewm
        RSI = 100 - 100 / (1 + RS)

        data_res['RSI'] = RSI

        return data_res['RSI']