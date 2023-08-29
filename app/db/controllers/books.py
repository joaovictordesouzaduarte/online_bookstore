from ..models.book import Book as BookModel
from ..schemas.book import Book as BookSchema
from sqlalchemy.orm import Session
from .genres import get_book_genre_by_name


def creating_new_book(book: BookSchema, db: Session) -> BookSchema:
    genre_id = get_book_genre_by_name(book.genre, db).id

    if genre_id is None:
        raise Exception(
            f"O gênero {book.name} não foi encontrado no banco de dados. Cadastre-o."
        )
    db_model = BookModel(
        categories=book.categories,
        published_date=book.published_date,
        price=book.price,
        stock_quantity=book.stock_quantity,
        available_status=book.available_status,
        title=book.title,
        synophis=book.synophis,
        cover_image_url=book.cover_image_url,
        format=book.format,
        genres_id=genre_id,
    )
    return db_model
    # db_connection.add(db_genre)
    # db_connection.commit()
    # db_connection.refresh(db_genre)
    # db_connection.close()


def get_all_books(db_connection: Session) -> BookSchema:
    book_list = db_connection.query(BookModel).all()
    return book_list
