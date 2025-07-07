"""
CORE portfolio candidate analyzer component:
Sends/Receives data from Integrator component: <-> Database, <- API Data Retriever;
Analyzes indicators and factors based on personal Investing Manifest;
Gets value from APIs and compares against required values;
Returns grading for each compared variable;
"""

from . import api_retriever_cmp as retriever


class CoreStock:
    """Class for CORE stock analysis"""

    def __init__(self, ticker: str):
        self.cash_flows_data = None
        self.income_statements_data = None
        self.ticker = ticker
        self.core_item_retriever = None

    def get_cash_flows(self):
        """Get Cash Flows data for the ticker if they were not retrieved before."""
        if self.cash_flows_data is None:
            self.cash_flows_data = self.core_item_retriever.retrieve_stock_fundamental_data("CASH_FLOW")
        return self.cash_flows_data

    def get_income_statements(self):
        """Get Income Statements data for the ticker if they were not retrieved before."""
        if self.income_statements_data is None:
            self.income_statements_data = self.core_item_retriever.retrieve_stock_fundamental_data("INCOME_STATEMENT")
        return self.income_statements_data

    def calculate_fcf(self):
        """Calculate Free Cash Flows for the ticker for last 5 years"""
        self.get_cash_flows()
        self.get_income_statements()
        cash_flow_from_operating_activities = self.cash_flows_data['annualReports'][0]['operatingCashflow']
        interest_expense = self.income_statements_data['annualReports'][0]['interestExpense']

    def core_analyze(self):
        """Create a retriever for specified ticket and invoke Free Cash Flow calculation."""
        self.core_item_retriever = retriever.StockRetriever(self.ticker)
        self.calculate_fcf()