from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class Book(BaseModel):
    id: str
    title: str
    author: str
    isbn: str
    published_date: str
    copies: int

books_db = []

@router.post("/", response_model=Book)
def create_book(book: Book):
    book.id = str(uuid4())
    books_db.append(book)
    return book

@router.get("/", response_model=List[Book])
def get_books():
    return books_db

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: str, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            updated_book.id = book_id
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
def delete_book(book_id: str):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")