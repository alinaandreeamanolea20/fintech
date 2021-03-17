from fastapi import FastAPI
from api import stocks

app = FastAPI(debug=True)
app.include_router(stocks.router)


@app.on_event("startup")
async def startup():
    pass

