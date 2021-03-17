from pydantic import BaseModel, Field


class NewStock(BaseModel):
    name: str = Field(description="Short name of the stock, eg MSFT, TSLA")

