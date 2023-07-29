from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    Float,
    Text,
    Enum,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from ..db_setup import Base

import enum

from .mixins import Timestamp


class Format(enum.Enum):
    hardcover = 1
    paperback = 2
    ebook = 3


class Book(Timestamp, Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    categories = Column(String, nullable=False)
    published_date = Column(Date, nullable=True)
    genres_id = Column(Integer, ForeignKey("genres.id"))
    authors_id = Column(Integer, ForeignKey("authors.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    publishers = relationship("Publisher", back_populates="books")
    languages = relationship("Language", back_populates="books")
    authors = relationship("Author", back_populates="books")
    genres = relationship("Genre", back_populates="books")
    format = Column(Enum(Format))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    available_status = Column(Boolean, default=True)
    synophis = Column(String(length=250), nullable=True)
    title = Column(String, index=True)
    cover_image_url = Column(URLType, nullable=True)


class Author(Timestamp, Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="authors")


class Publisher(Timestamp, Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="publishers")


class Language(Timestamp, Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="languages")


class Genre(Timestamp, Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="genres")
