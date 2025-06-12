from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class Member(BaseModel):
    id: str
    name: str
    email: str
    membership_date: str

members_db = []

@router.post("/", response_model=Member)
def create_member(member: Member):
    member.id = str(uuid4())
    members_db.append(member)
    return member

@router.get("/", response_model=List[Member])
def get_members():
    return members_db

@router.get("/{member_id}", response_model=Member)
def get_member(member_id: str):
    for member in members_db:
        if member.id == member_id:
            return member
    raise HTTPException(status_code=404, detail="Member not found")

@router.put("/{member_id}", response_model=Member)
def update_member(member_id: str, updated_member: Member):
    for i, member in enumerate(members_db):
        if member.id == member_id:
            updated_member.id = member_id
            members_db[i] = updated_member
            return updated_member
    raise HTTPException(status_code=404, detail="Member not found")

@router.delete("/{member_id}")
def delete_member(member_id: str):
    for i, member in enumerate(members_db):
        if member.id == member_id:
            del members_db[i]
            return {"message": "Member deleted"}
    raise HTTPException(status_code=404, detail="Member not found")