from pydantic import BaseModel, Field


class NewStock(BaseModel):
  name: str = Field(description="Short name of the stock, eg MSFT, TSLA")


class StockInfo(BaseModel):
  id: str = Field(description="Short name of the stock, eg MSFT, TSLA")
  sector: str = Field(description="")
  employees: int = Field(description="")

  # city: str = Field(description="")
  # country: str = Field(description="")
  # previousClose: float = Field()
  # marketOpen: float = Field()
  # average: float = Field()
  class Config:
    orm_mode = True
