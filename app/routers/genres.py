from fastapi import APIRouter, Depends, HTTPException
from db.db_setup import get_db
from db.schemas.genre import Genre
from sqlalchemy.orm import Session
from typing import Optional
from db.controllers.genres import (
    create_book_genre,
    get_book_genre_by_id,
    get_book_genre_by_name,
    get_books_genres,
)

router = APIRouter()


@router.post("/genre")
async def creating_book_genre(genre: Genre, db: Session = Depends(get_db)):
    """
    Creating new book's genrer
    """
    try:
        create_book_genre(genre, db)
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))

    return "Gênero cadastrado com sucesso"


@router.get("/genre/{id}")
async def get_genre(id: int, db: Session = Depends(get_db)):
    """
    Retrieve genre by id
    """
    try:
        book_genre = get_book_genre_by_id(id, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    return book_genre


@router.get("/genres")
async def get_books_gender(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Retrieve genre by name
    """
    try:
        if name:
            book_genre = get_book_genre_by_name(name, db)
        else:
            book_genre = get_books_genres(db)
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))

    return book_genre
