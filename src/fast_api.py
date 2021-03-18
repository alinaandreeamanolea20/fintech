from fastapi import FastAPI
from api import stocks
from finance.repo import StocksRepo

app = FastAPI(debug=True)
app.include_router(stocks.router)


@app.on_event("startup")
async def startup():
    repo = StocksRepo()
    repo.load()


