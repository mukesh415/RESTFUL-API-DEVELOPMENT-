from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class Loan(BaseModel):
    id: str
    book_id: str
    member_id: str
    loan_date: str
    return_date: str

loans_db = []

@router.post("/", response_model=Loan)
def create_loan(loan: Loan):
    loan.id = str(uuid4())
    loans_db.append(loan)
    return loan

@router.get("/", response_model=List[Loan])
def get_loans():
    return loans_db

@router.get("/{loan_id}", response_model=Loan)
def get_loan(loan_id: str):
    for loan in loans_db:
        if loan.id == loan_id:
            return loan
    raise HTTPException(status_code=404, detail="Loan not found")

@router.put("/{loan_id}", response_model=Loan)
def update_loan(loan_id: str, updated_loan: Loan):
    for i, loan in enumerate(loans_db):
        if loan.id == loan_id:
            updated_loan.id = loan_id
            loans_db[i] = updated_loan
            return updated_loan
    raise HTTPException(status_code=404, detail="Loan not found")

@router.delete("/{loan_id}")
def delete_loan(loan_id: str):
    for i, loan in enumerate(loans_db):
        if loan.id == loan_id:
            del loans_db[i]
            return {"message": "Loan deleted"}
    raise HTTPException(status_code=404, detail="Loan not found")