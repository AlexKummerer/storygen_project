from fastapi import APIRouter

router = APIRouter()

@router.post("/subscribe")
async def subscribe_user(user_id: int, plan: str):
    return {"message": "User subscribed to plan"}

@router.get("/subscription_status")
async def subscription_status(user_id: int):
    return {"status": "Subscription status for the user"}
