"""
CORE portfolio candidate analyzer component:
Sends/Receives data from Integrator component: <-> Database, <- API Data Retriever;
Analyzes indicators and factors based on personal Investing Manifest;
Gets value from APIs and compares against required values;
Returns grading for each compared variable;
"""

import json
from . import api_retriever_cmp as retriever


class CoreStock:
    """Class for CORE stock analysis"""

    def __init__(self, ticker: str):
        self.ticker = ticker

    def calculate_fcf(self, core_item_retriever):
        """Calculate Free Cash Flows for the ticker for last 5 years"""
        # loaded_data = json.loads(data)
        core_item_data = core_item_retriever.retrieve_stock_fundamental_data("CASH_FLOW")
        print(core_item_data['annualReports'][0])

    def core_analyze(self, expected_function="OVERVIEW"):
        """Retrieve required data for the stock ticker. Method is invoked on ticker defined
        during class creation but expected dataset must be specified in expected_function.
        OVERVIEW argument is passed by default. """

        core_item_retriever = retriever.StockRetriever(self.ticker)

        self.calculate_fcf(core_item_retriever)