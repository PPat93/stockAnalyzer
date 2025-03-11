""" 
Plotter component:
Sends/Receives data from Integrator: <- Analyzer, <- Database, -> Mailer;
Creates graphs for content of notification emails;
"""

import matplotlib.pyplot as plt


class Plotter:
    """Class for graphs plotting"""

    def __init__(self) -> None:
        pass

    def plot_one_graph(
        self, data, graph_name, ticker, start_date, end_date, *horizontal_lines
    ):

        fig, ax = plt.subplots()
        ax.plot(data)
        ax.legend()
        ax.set_xlabel("Date")
        ax.set_ylabel(graph_name)
        ax.set_title(f"{ticker} Stock {graph_name} graph ({start_date} to {end_date})")
        for line in horizontal_lines:
            ax.axhline(y=line, c="green", linewidth=0.5, zorder=0, linestyle="--")
        plt.show()

    # plot_one_graph([1, 2, 3], "MACD", "NVDA", "1", "12", 4, 5, 6)