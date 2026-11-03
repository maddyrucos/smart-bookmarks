from fastapi import FastAPI
from .api import api_router

app = FastAPI(
    title="Smart Bookmarks Backend",
    description="Backend service for managing smart bookmarks.",
    version="0.0.1",
)

app.include_router(api_router)