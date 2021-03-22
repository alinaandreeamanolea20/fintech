import yfinance


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
