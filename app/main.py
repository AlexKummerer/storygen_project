from fastapi import FastAPI
from app.api.v1.endpoints import users, stories, subscriptions

app = FastAPI()



app.include_router(users.router, prefix="/api/v1/users")
app.include_router(stories.router, prefix="/api/v1/stories")
app.include_router(subscriptions.router, prefix="/api/v1/subscriptions")
