import os
import json

from singleton import SingletonMeta
from finance.stock import Stock


class StockNotFound(Exception):
    pass


class StocksRepo(metaclass=SingletonMeta):
    stocks = []
    file = 'stocks.json'

    def add(self, name: str) -> Stock:
        new_stock = Stock(name)
        self.stocks.append(new_stock)
        self.__save_to_config(name)
        return new_stock

    def get_all(self):
        return self.stocks

    def get_by_id(self, id: str):
        ids = [s for s in self.stocks if s.id == id]
        if not ids:
            raise StockNotFound()
        return ids[0]

    def load(self):
        if not os.path.exists(self.file):
            self.stocks = []
        else:
            with open(self.file, 'r') as f:
                current_config = json.loads(f.read())
            for name in current_config:
                self.stocks.append(Stock(name))

    def __save_to_config(self, name):
        if not os.path.exists(self.file):
            f = open(self.file, 'w')
            f.write(json.dumps([]))
            f.close()
        f = open(self.file, 'r')
        current_config = json.loads(f.read())
        f.close()
        current_config.append(name)
        with open(self.file, 'w') as f:
            f.write(json.dumps(current_config))


