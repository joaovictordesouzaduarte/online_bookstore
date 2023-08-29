from fastapi import APIRouter, Depends, HTTPException
from db.db_setup import get_db
from db.schemas.language import Language
from sqlalchemy.orm import Session
from db.controllers.languages import create_book_language, get_book_language

router = APIRouter()


@router.post("/language")
async def creating_book_language(language: Language, db: Session = Depends(get_db)):
    """
    Creating new book's genrer
    """
    try:
        create_book_language(language, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    return "Língua cadastrado com sucesso"


@router.get("/language/{id}")
async def get_language_by_id(id: int, db: Session = Depends(get_db)):
    """
    Creating new book's language
    """
    try:
        book_language = get_book_language(id, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    return book_language
