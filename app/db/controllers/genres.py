from ..models.book import Genre as GenreModel
from ..schemas.genre import Genre as GenreSchema
from sqlalchemy.orm import Session


def create_book_genre(genre: GenreSchema, db_connection: Session) -> GenreSchema:
    db_genre = GenreModel(name=genre.name)
    db_connection.add(db_genre)
    db_connection.commit()
    db_connection.refresh(db_genre)
    db_connection.close()


def get_book_genre_by_id(id: int, db_connection: Session) -> GenreSchema:
    #     """
    #     Searching a user by id
    #     """

    genre = db_connection.query(GenreModel).filter(GenreModel.id == id).first()

    if genre is None:
        raise Exception(f"O gênero com o id {id} não foi encontrado no banco de dados.")
    return genre


def get_book_genre_by_name(name: str, db_connection: Session) -> GenreSchema:
    """
    Searching a user by id
    """

    genre = (
        db_connection.query(GenreModel)
        .filter(GenreModel.name == name.capitalize())
        .first()
    )

    if genre is None:
        raise Exception(
            f"O gênero com o nome {name} não foi encontrado no banco de dados. Por favor, cadastre-o."
        )
    return genre


def get_books_genres(db_connection: Session) -> GenreSchema:
    """
    Searching a user by id
    """

    genre = db_connection.query(GenreModel).all()

    if genre is None:
        raise Exception(f"Nenhum gênero foi cadastrado.")
    return genre
