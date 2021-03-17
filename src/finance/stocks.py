import yfinance

from singleton import SingletonMeta


class StocksRepo(metaclass=SingletonMeta):
    stocks = []

    def add(self, name: str):
        ticker = yfinance.Ticker(name)
        self.stocks.append(ticker)

    def get_all(self):
        return self.stocks

