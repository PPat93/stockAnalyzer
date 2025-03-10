"""
Utilities:
File that gathers utility bits used all across the project.
"""

import pandas_market_calendars as pmcal

def calculate_window(start_date, end_date, market):
    """Calculate trading days between specified dates for the provided exchange.
    Calculation excludes weekends and holidays"""

    exchange = pmcal.get_calendar(market)
    schedule = exchange.schedule(start_date=start_date, end_date=end_date)

    return len(schedule)