from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
async def get_users():
    all_users = [{"name": "João Victor"}, {"name": "Márcia"}]
    return all_users


# async def
