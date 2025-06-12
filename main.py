from fastapi import FastAPI
from app import books, members, loans

app = FastAPI(title="Library System API")

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])