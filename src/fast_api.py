from fastapi import FastAPI
from api import stocks
from finance.repo import StocksRepo, StockNotFound
from fastapi.responses import JSONResponse

app = FastAPI(debug=True)
app.include_router(stocks.router)


@app.exception_handler(StockNotFound)
async def stock_not_found(request, exception: StockNotFound):
    return JSONResponse(status_code=404, content="The specified stock was not added.")


@app.on_event("startup")
async def startup():
    repo = StocksRepo()
    repo.load()


