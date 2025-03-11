"""
MACD calcs:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment. For now MACD is limited to the 
shorter period.
"""

import numpy as np
from . import ema_clc as ema

# MACD = 12-PeriodEMA − 26-PeriodEMA
# EMAs - 12 periods and 26 periods Exponential Moving Average


class MACD:
    """Class for MACD calculation and all utilities around it"""

    def __init__(self, ticker: str, timeframe: str) -> object:
        self.ticker = ticker
        self.timeframe = timeframe

    def calc_macd(self):
        """Retrieve specified stock data range and calculate its MACD"""

        if self.timeframe == "short":
            period_s = 12
            period_l = 26
            s_line = 9
        elif self.timeframe == "long":
            period_s = 24
            period_l = 52
            s_line = 18

        local_ema_s = ema.EMA(self.ticker, period_s)
        local_ema_l = ema.EMA(self.ticker, period_l)

        ema_s = local_ema_s.calc_ema()
        ema_l = local_ema_l.calc_ema()

        # Calculate MACD (the difference between shorter-period EMA and longer-period EMA)
        macd = ema_s["ema"] - ema_l["ema"]
        signal = macd.ewm(span=s_line, adjust=False).mean()

        return macd, signal

    def trade_signals(self):
        """Return buy/sell points on the basis of MACD and it's signal line"""

        macd, signal = self.calc_macd()

        signals = np.where(macd > signal, 1, -1)
        signals = np.where(macd.isnull(), 0, signals)