from fastapi import APIRouter, Depends, HTTPException
from db.db_setup import get_db
from sqlalchemy.orm import Session
from db.schemas.book import Book as BookSchema
from db.controllers.books import creating_new_book, get_all_books

# from db.schemas.user
router = APIRouter()


@router.post("/book")
async def create_book(book: BookSchema, db: Session = Depends(get_db)):
    try:
        new_book = creating_new_book(book, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return new_book


@router.get("/books")
async def get_book_by_criteria(db: Session = Depends(get_db)):
    try:
        books = get_all_books(db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return books
