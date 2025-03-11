"""
Fibonacci Retracements calcs:
Theoretical lines that helps to assess critical points on charts such
as - supports, resistances, target prices, trend reversals etc. They 
are calculated by taking two important points from the chart (e.g. 52 
weeks low and high) subtracting them and dividing calculated distance
by specified percentage ratios: 23.6%, 38.2%, 50%, 61.8%, and 100%. 
FR must be used with other TA items, as it usually works as the self-
-fulfilling prophecy. It's worth to consider a little bit smaller/bigger
percentages to get ahead other traders.
"""

import yfinance as yf


class FibonacciRetrace:
    """Class for Fibonacci Retracements calculation and all utilities around it"""

    def __init__(
        self, ticker: str, start_date: str, end_date: str, trend_direction: str
    ) -> object:
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.trend_direction = trend_direction

    # TODO get rid of trend direction argument and replace it with rsi/macd automatic calculation
    def calc_fib_retr(self):
        """Calculate and return Fibonacci Retracement lines"""

        res = yf.download(tickers=self.ticker, start=self.start_date, end=self.end_date)

        res_highest = res["Close"].max()
        res_lowest = res["Close"].min()

        lvl_rates = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
        lvl_lines = []

        dif = res_highest - res_lowest

        for x in lvl_rates:
            if self.trend_direction == "up":
                lvl_lines.append(res_highest - x * dif)
            elif self.trend_direction == "down":
                lvl_lines.append(res_lowest + x * dif)

        return lvl_lines