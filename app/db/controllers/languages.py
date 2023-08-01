from ..models.book import Language as LanguageModel
from ..schemas.language import Language as LanguageSchema
from sqlalchemy.orm import Session


def create_book_language(
    language: LanguageSchema, db_connection: Session
) -> LanguageSchema:
    db_language = LanguageModel(name=language.name)
    db_connection.add(db_language)
    db_connection.commit()
    db_connection.refresh(db_language)
    db_connection.close()


def get_book_language(id: int, db_connection: Session) -> LanguageSchema:
    #     """
    #     Searching a user by id
    #     """

    language = db_connection.query(LanguageModel).filter(LanguageModel.id == id).first()
    return language
