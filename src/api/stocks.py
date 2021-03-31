from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.models import NewStock, StockInfo, StockRecommendations, NewDiagram
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


@router.get("/{stock_id}/recommendations")
def get_stock_recommendations(stock_id: str):
    repo = StocksRepo()
    stock = repo.get_by_id(stock_id)
    if not stock:
        return JSONResponse(status_code=404, content="The specified stock was not added.")
    return StockRecommendations.from_orm(stock[0])


@router.post("/{stock_id}/diagram")
def create_diagram(stock_id: str, body: NewDiagram):
    repo = StocksRepo()
    stock = repo.get_by_id(stock_id)
    stock.draw_diagram(body.start_date, body.end_date)
