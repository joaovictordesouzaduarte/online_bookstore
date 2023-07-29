from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    categories: str
    published_date: datetime
    price: float
    stock_quantity: int
    available_status: bool | True

    # synophis:
    class Config:
        orm_mode = True
