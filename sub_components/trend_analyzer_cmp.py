"""
Trend analyzer component:
Sends/Receives data from Integrator component: <-> Database, <- API Data Retriever, ->Mailer;
Compares received stock price with previously stored reference price/time data;
Saves compared data as a new reference if expected;
Remove old reference data if expected;
"""

import calcs.rsi_clc as rsi
import calcs.macd_clc as macd
import calcs.ema_clc as ema
import calcs.fibonacci_retracements_clc as fibs
from . import api_retriever_cmp as retriever


class TrendStock:
    """Class for entire stock analysis."""

    def __init__(
            self,
            ticker: str,
            start_date: str,
            end_date: str,
            timeframe: str,
            period: int,
            trend_direction: str,
    ) -> bool:
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.end_date = end_date
        self.timeframe = timeframe
        self.period = period
        self.trend_direction = trend_direction
        self.stock_retriever = retriever.StockRetriever(self.ticker)
        self.adjust = False

    def run_trend_analysis(self):
        """Method allowing for complete stock trend analysis run from one place"""

        ema_new = ema.EMA(self.ticker, self.period)
        fibonacci_new = fibs.FibonacciRetrace(
            self.ticker, self.start_date, self.end_date, self.trend_direction
        )
        rsi_new = rsi.RSI(self.ticker, self.start_date, self.end_date, adjust=self.adjust)
        macd_new = macd.MACD(self.ticker, self.timeframe)

        latest_price = float((self.stock_retriever.retrieve_last_stock_price()))

        calculated_rsi = rsi_new.calc_rsi()
        calculated_fibonacci = fibonacci_new.calc_fib_retr()
        calculated_ema = ema_new.calc_ema()
        calculated_macd = macd_new.calc_macd()

        trend_is_reversed = (
            False  # TODO bool returned with a value if the trend was reversed
        )

        return trend_is_reversed