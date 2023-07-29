from fastapi import APIRouter

# from db.schemas.
router = APIRouter()


@router.post("/book")
async def create_book(book):
    pass
