from pydantic import BaseModel, Field
from typing import List


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


class StockRecommendations(BaseModel):
  class Config:
    orm_mode = True

  id: str = Field(description="Short name of the stock, eg MSFT, TSLA")
  rec: List[dict] = Field(description="Recommendations by firms")
