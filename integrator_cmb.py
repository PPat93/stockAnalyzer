"""
Integrator comb:
Integrates modules;
Passes flags invoking actions;
Holds actions confirmations;

API Data Retriever -> Integrator -> Analyzer
Database -> Integrator -> Analyzer
Analyzer -> Integrator -> Database
Analyzer -> Integrator -> Mailer
Database -> Integrator -> Mailer
"""

from sub_cmbs.analyzer_cmb import run_trend_analysis


def invoke_trend_analysis(ticker: str, start_date: str, end_date: str, timeframe: str):
    """Execute trend analysis"""

    is_trend_reversed = run_trend_analysis(ticker, start_date, end_date, timeframe)
    # return analysis_result TODOs

invoke_trend_analysis("NVDA", "2024-05-02", "2024-07-07", "long")
