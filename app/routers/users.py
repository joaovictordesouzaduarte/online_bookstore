from fastapi import APIRouter, Depends, HTTPException
from db.db_setup import get_db
from db.schemas.user import User
from sqlalchemy.orm import Session
from db.controllers.users import create_user, get_all_users, get_user, delete_user

router = APIRouter()


@router.post("/user")
async def insert_users(
    user: User,
    db: Session = Depends(get_db),
):
    """
    Inserting new user into the database <br>
    Fields: <br>
        **username**: Should be string <br>
        **email**: An valid E-mail <br>
        **password**: An valid password that will be hashed <br>
        **is_active**: Boolean <br>
    """
    try:
        create_user(user, db)
    except Exception as ex:
        raise Exception("Houve um erro ao inserir os dados no banco")

    return user


@router.get("/users")
async def get_users(
    db: Session = Depends(get_db),
):
    users = get_all_users(db)
    return users


@router.get("/user/{user_id}")
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = get_user(user_id, db)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"Nenhum usuário encontrado com o ID {user_id}"
        )
    return user


@router.delete("/delete/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    """"""
    try:
        delete_user(user_id, db)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return f"Usuário {id} excluído com sucesso."


# async def
