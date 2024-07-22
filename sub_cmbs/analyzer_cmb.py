"""
Analyzer comb:
Sends/Receives data from Integrator Comb: <-> Database, <- API Data Retriever, ->Mailer;
Compares received stock price with previously stored reference price/time data;
Saves compared data as a new reference if expected;
Remove old reference data if expected;
"""

import calc_hex.rsi_hex as rsi
import calc_hex.macd_hex as macd
import calc_hex.ema_hex as ema
import calc_hex.fibonacci_retracements_hex as fibs
from . import api_retriever_cmb as retriever


class Stock:
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

    def run_trend_analysis(self):
        """Method allowing for complete stock trend analysis run from one place"""

        ema_new = ema.EMA(self.ticker, self.period)
        fibonacci_new = fibs.FibonacciRetrace(
            self.ticker, self.start_date, self.end_date, self.trend_direction
        )
        rsi_new = rsi.RSI(self.ticker, self.start_date, self.end_date)
        macd_new = macd.MACD(self.ticker, self.timeframe)

        latest_price = float(
            (retriever.retrieve_last_stock_price(self.ticker))[0].get("last")
        )

        calculated_rsi = rsi_new.calc_rsi()
        calculated_fibonacci = fibonacci_new.calc_fib_retr()
        calculated_ema = ema_new.calc_ema()
        calculated_macd = macd_new.calc_macd()

        trend_is_reversed = (
            False  # TODO bool returned with a value if the trend was reversed
        )

        return trend_is_reversed
