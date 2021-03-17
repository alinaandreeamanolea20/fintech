from fastapi import APIRouter

from api.models import NewStock
from finance.stocks import StocksRepo

router = APIRouter(prefix="/stocks")


@router.post("/")
def add_stock(new_stock: NewStock):
    repo = StocksRepo()
    repo.add(new_stock.name)


@router.get("/")
def get_stocks():
    repo = StocksRepo()
    return repo.get_all()

