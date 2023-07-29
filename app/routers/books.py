from fastapi import APIRouter

# from db.schemas.user
router = APIRouter()


@router.post("/book")
async def create_book(book):
    pass


@router.get("/books")
async def get_book_by_criteria():
    return {"name": "Prisioneiros da Geografia"}
