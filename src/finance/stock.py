import yfinance


class Stock:
  def __init__(self, id: str):
    self.ticker = yfinance.Ticker(id)
    self.id = id
    self.employees = self.ticker.info['fullTimeEmployees']
    self.sector = self.ticker.info['sector']
