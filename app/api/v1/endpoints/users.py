from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register_user(email: str, password: str):
    return {"message": "User registered"}

@router.post("/login")
async def login_user(email: str, password: str):
    return {"token": "JWT token goes here"}
