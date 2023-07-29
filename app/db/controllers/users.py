from ..models.user import User as UserModel
from ..schemas.user import User as UserSchema
from .hash_password import get_password_hash
from sqlalchemy.orm import Session
from sqlalchemy import text, delete


def create_user(user: UserSchema, db_connection: Session) -> UserModel:
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active,
    )
    db_connection.add(db_user)
    db_connection.commit()
    db_connection.refresh(db_user)
    db_connection.close()
    return "Usuário cadastrado com sucesso"


def get_all_users(db_connection: Session) -> list[UserSchema]:
    """"""
    users_list = db_connection.query(UserModel).all()
    return users_list


def get_user(id: int, db_connection: Session) -> UserSchema:
    """
    Searching a user by id
    """

    user = db_connection.query(UserModel).filter(UserModel.id == id).first()
    return user


def delete_user(id: int, db_connection: Session) -> UserSchema:
    db_connection.query(UserModel).filter(UserModel.id == id).delete()
    db_connection.commit()
