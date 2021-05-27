from fastapi import APIRouter, Query
from core.security import create_access_token
from model.user import CreateUser

router = APIRouter()

@router.post("/register")
async def register(user: CreateUser):
    print("user register")
    return create_access_token(data={"username": user.username, "email": user.email})
