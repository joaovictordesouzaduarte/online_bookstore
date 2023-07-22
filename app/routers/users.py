from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
    all_users = [{"name": "João Victor"}, {"name": "Márcia"}]
    return all_users
