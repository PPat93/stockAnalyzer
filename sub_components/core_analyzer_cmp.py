"""
CORE portfolio candidate analyzer component:
Sends/Receives data from Integrator component: <-> Database, <- API Data Retriever;
Analyzes indicators and factors based on personal Investing Manifest;
Gets value from APIs and compares against required values;
Returns grading for each compared variable;
"""

from . import api_retriever_cmp as retriever

class CoreStock:
    def __init__(self, ticker: str):
        self.ticker = ticker

    def core_analyze(self):
        core_item = retriever.StockRetriever(self.ticker)
        core_item_data = core_item.retrieve_stock_dataset_data("cash-flow-statement-growth")
        print(core_item_data)