"""
Integrator component:
Integrates modules;
Passes flags invoking actions;
Holds actions confirmations;

API Data Retriever -> Integrator -> Analyzer
Database -> Integrator -> Analyzer
Analyzer -> Integrator -> Database
Analyzer -> Integrator -> Mailer
Database -> Integrator -> Mailer
"""

import time
from sub_components.trend_analyzer_cmp import TrendStock as TrendStck
from sub_components.core_analyzer_cmp import CoreStock as CoreStck


stocks = {}


def check_dictionary(dictionary, string):
    """Check if any key in dictionary includes a string, if so - return these keys"""
    if any(string in key for key in dictionary):
        return list(key for key in dictionary if string in key)


def invoke_trend_analysis(
        ticker: str,
        start_date: str,
        end_date: str,
        timeframe: str,
        period: int,
        trend_direction: str,
):
    """Execute trend analysis"""

    # Check if stocks dictionary already has ticker stock class instance created
    check_existing = check_dictionary(stocks, ticker)

    # if stock instance already exists - create new stock instance, remove old one
    # and replace key for the new one wwith current timestamp
    if check_existing:
        timestamp = int(time.time())
        new_key = ticker + str(timestamp)
        current_stock = check_existing[0]
        stocks[new_key] = TrendStck(
            ticker, start_date, end_date, timeframe, period, trend_direction
        )
        del stocks[current_stock]
        current_stock = new_key
    # if stock instance does not exist, just create new stock instance and include
    # it in stocks dictionary with ticker name plus current timestamp
    else:
        timestamp = int(time.time())
        current_stock = ticker + str(timestamp)
        stocks[current_stock] = TrendStck(
            ticker, start_date, end_date, timeframe, period, trend_direction
        )

    # run trend analysis on freshly created stock instance
    is_trend_reversed = stocks[current_stock].run_trend_analysis()

    # return analysis_result TODOs

def invoke_core_analysis(ticker: str):
    core_stock = CoreStck(ticker)
    core_stock.core_analyze()


invoke_core_analysis("CMA")
# invoke_trend_analysis("CMA", "2025-01-01", "2025-02-17", "long", 26, "up")
# invoke_trend_analysis("NVDA", "2024-05-02", "2024-07-07", "long", 26, "up")