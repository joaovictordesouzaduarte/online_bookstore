from pydantic import BaseModel, HttpUrl
from datetime import datetime
from enum import Enum
from typing import Optional


class Format(Enum):
    hardcover = 1
    paperback = 2
    ebook = 3


class Book(BaseModel):
    categories: str
    published_date: datetime
    price: float
    stock_quantity: int
    available_status: Optional[bool] = True
    title: str
    synophis: str
    cover_image_url: HttpUrl
    format: Format
    genre: str

    # synophis:
    class Config:
        orm_mode = True
