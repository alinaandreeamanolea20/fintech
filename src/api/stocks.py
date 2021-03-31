from fastapi import APIRouter
from fastapi.responses import FileResponse

from api.models import NewStock, StockInfo, StockRecommendations, NewDiagram
from finance.repo import StocksRepo

import os

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


@router.get("/{stock_id}/recommendations")
def get_stock_recommendations(stock_id: str):
    repo = StocksRepo()
    stock = repo.get_by_id(stock_id)
    return StockRecommendations.from_orm(stock)


@router.post("/{stock_id}/diagram")
def create_diagram(stock_id: str, body: NewDiagram):
    repo = StocksRepo()
    stock = repo.get_by_id(stock_id)
    stock.draw_diagram(body.start_date, body.end_date)


@router.get("/diagram")
def get_diagram(stock_id: str):
    current_dir = os.getcwd()
    path = f"{current_dir}/diagram-{stock_id}.png"
    return FileResponse(path)
