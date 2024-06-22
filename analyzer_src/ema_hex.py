"""
EMA hex:
Calculates Exponential Moving Average for a given stock ticker on specified period.
Most recent data points are more important than older ones. Therefore, it reacts 
more the more recent price change is. Usually used to find buy/sell signals.
Most frequently used periods are: 12, 26, 50, 200 days.
"""

from datetime import date, timedelta
import yfinance as yf

# EMA = Price(today)×k+EMA(yesterday)×(1−k); where: k=2÷(N+1), n = number of days
# the above calculation formula assumes 1 day = 1 period


def calc_ema(ticker: str, period: int):
    """Retrieve specified stock data and calculate its EMA for specified period"""

    current_date = date.today()
    potential_public_holidays = 20

    # Include potential holidays - as there are multiple holidays/free days/no trading
    # during longer periods retrieved;
    if period < 7:
        potential_public_holidays = 2
    elif period > 150:
        potential_public_holidays = 40

    # Increase number of data points to be retrieved by the number of potential non-trading days;
    period_including_non_working_days = (
        include_weekends_in_days_substract(date.today(), period)
        + potential_public_holidays
    )

    # Calculate expected retrieval date
    start_date = date.today() - timedelta(days=period_including_non_working_days)
    data_retrieved = yf.download(ticker, start=start_date, end=current_date)

    # Adjust retrieved data to have specified periods
    data_retrieved = data_retrieved.tail(period)

    # Calculate Exponential Moving Average
    data_retrieved["ema"] = data_retrieved["Close"].ewm(span=period, adjust=False).mean()

    return data_retrieved


def include_weekends_in_days_substract(date, workdays_to_substract: int):
    """Include weekends in the working days provided in workdays_to_substract to
    calculate how many days actually needs to be substracted to reach the
    period of workdays_to_substract workdays"""
    all_days_to_substract = 0
    temp_date = date

    # If a day is non-weekend one, lower workdays_to_substract by one
    while workdays_to_substract > 0:
        temp_date -= timedelta(days=1)
        if temp_date.weekday() < 5:
            workdays_to_substract -= 1
        all_days_to_substract += 1

    return all_days_to_substract
