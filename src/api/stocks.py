from fastapi import APIRouter

from api.models import NewStock, StockInfo
from finance.repo import StocksRepo

router = APIRouter(prefix="/stocks")


@router.post("/", response_model=StockInfo)
def add_stock(new_stock: NewStock):
    repo = StocksRepo()
    new_stock = repo.add(new_stock.name)
    return StockInfo.from_orm(new_stock)


@router.get("/")
def get_stocks():
    repo = StocksRepo()
    return list(map(StockInfo.from_orm, repo.get_all()))

