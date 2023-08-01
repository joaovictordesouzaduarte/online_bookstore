from ..models.book import Genre as GenreModel
from ..schemas.genre import Genre as GenreSchema
from sqlalchemy.orm import Session


def create_book_genre(genre: GenreSchema, db_connection: Session) -> GenreSchema:
    db_genre = GenreModel(name=genre.name)
    db_connection.add(db_genre)
    db_connection.commit()
    db_connection.refresh(db_genre)
    db_connection.close()


def get_book_genre(id: int, db_connection: Session) -> GenreSchema:
    #     """
    #     Searching a user by id
    #     """

    genre = db_connection.query(GenreModel).filter(GenreModel.id == id).first()
    return genre
