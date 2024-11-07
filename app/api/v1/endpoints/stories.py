from fastapi import APIRouter

router = APIRouter()

@router.get("/generate_story")
async def generate_story():
    return {"message": "Story generation endpoint"}


@router.post("/generate_story")
async def generate_story(prompt: str):
    return {"story": "Generated story goes here"}