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
        self.balance_sheet = None
        self.ticker = ticker
        self.core_item_retriever = None
        self.fcff_array = []
        self.total_debt = None

    def get_cash_flows(self):
        """Get Cash Flows data for the ticker if they were not retrieved before."""
        if self.cash_flows_data is None:
            self.cash_flows_data = self.core_item_retriever.retrieve_stock_fundamental_data("CASH_FLOW")
        return self.cash_flows_data

    def get_balance_sheet(self):
        """Get Balance Sheet data for the ticker if they were not retrieved before."""
        if self.balance_sheet is None:
            self.balance_sheet = self.core_item_retriever.retrieve_stock_fundamental_data("BALANCE_SHEET")
        return self.balance_sheet

    def get_income_statements(self):
        """Get Income Statements data for the ticker if they were not retrieved before."""
        if self.income_statements_data is None:
            self.income_statements_data = self.core_item_retriever.retrieve_stock_fundamental_data("INCOME_STATEMENT")
        return self.income_statements_data

    def calculate_fcff(self):
        """Calculate Free Cash Flows for the ticker for last 5 years
        Cash Flow from Operating Activities + Interest Expense - Tax Shield on Interest Expense - Capital Expenditures"""

        for i in range(5):
            self.get_cash_flows()
            self.get_income_statements()

            cash_flow_from_operating_activities = int(self.cash_flows_data['annualReports'][i]['operatingCashflow'])
            capex = int(self.cash_flows_data['annualReports'][i]['capitalExpenditures'])
            interest_expense = int(self.income_statements_data['annualReports'][i]['interestExpense'])

            # Calculate Tax Shield on Interest Expense
            income_tax_expense = int(self.income_statements_data['annualReports'][i]['incomeTaxExpense'])
            income_before_tax = int(self.income_statements_data['annualReports'][i]['incomeBeforeTax'])
            tax_rate = income_tax_expense / income_before_tax
            tax_shield_on_interest_expense = abs(tax_rate) * interest_expense
            i += 1
            self.fcff_array.append(cash_flow_from_operating_activities + interest_expense + tax_shield_on_interest_expense - capex)

        return self.fcff_array

    def calculate_debt_by_fcff(self):
        """Calculate Debt divided by Free Cash Flows indicator for the last 5 years.
        Total Debt / FCF"""

        self.get_cash_flows()
        self.get_balance_sheet()





    def core_analyze(self):
        """Create a retriever for specified ticket and invoke Free Cash Flow calculation."""
        self.core_item_retriever = retriever.StockRetriever(self.ticker)
        self.calculate_fcff()