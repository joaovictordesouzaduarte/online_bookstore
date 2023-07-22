from fastapi import FastAPI
from routers import users, books
from db.models import book, user, order
from db.db_setup import engine

book.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Bookstore",
    description="A booking store to connect books lovers",
    version="0.0.1",
    contact={"name": "João Victor", "email": "joaovictor@joaovictor.com"},
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
