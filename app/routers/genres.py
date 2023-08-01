from fastapi import APIRouter, Depends, HTTPException
from db.db_setup import get_db
from db.schemas.genre import Genre
from sqlalchemy.orm import Session
from db.controllers.genres import create_book_genre, get_book_genre

router = APIRouter()


@router.post("/genre")
async def creating_book_genre(genre: Genre, db: Session = Depends(get_db)):
    """
    Creating new book's genrer
    """
    try:
        create_book_genre(genre, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    return "Gênero cadastrado com sucesso"


@router.get("/genre/{id}")
async def get_genre_by_id(id: int, db: Session = Depends(get_db)):
    """
    Creating new book's genrer
    """
    try:
        book_genre = get_book_genre(id, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    return book_genre
