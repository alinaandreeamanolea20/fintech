import yfinance
from matplotlib import pyplot


class Stock:
    def __init__(self, id: str):
        self.ticker = yfinance.Ticker(id)
        self.id = id
        self.employees = self.ticker.info["fullTimeEmployees"]
        self.sector = self.ticker.info["sector"]
        self.__parse_recommendations(self.ticker.recommendations)

    def __parse_recommendations(self, recommendations_data):
        for item in recommendations_data.items():
            if item[0] == "Firm":
                firms = item[1].values.tolist()
            if item[0] == "To Grade":
                grades = item[1].values.tolist()
        self.rec = list(map(lambda x, y: {"firm": x, "grade": y}, firms, grades))

    def draw_diagram(self, start_date: str, end_date: str):
        # check all properties names of an object
        # print(self.ticker.__dict__.keys())
        # check all function names of an object
        # print(dir(self.ticker))
        history = self.ticker.history(start=start_date, end=end_date)
        close = history['Close']
        print(close)
        figure, axes = pyplot.subplots(figsize=(16, 9))

        axes.plot(close.index, close, label='Diagram of stock')

        axes.set_xlabel('Date')
        axes.set_ylabel('Close price')
        axes.legend()

        pyplot.savefig(f"diagram-{self.id}.png")
