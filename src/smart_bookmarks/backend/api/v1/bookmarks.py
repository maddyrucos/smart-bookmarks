from fastapi import APIRouter
from typing import List

from smart_bookmarks.entities.bookmark import (
    Bookmark, BookmarkCreate
)

bookmarks_router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])

@bookmarks_router.get("/")
async def get_bookmarks() -> List[Bookmark]:
    return []

@bookmarks_router.post("/")
async def create_bookmark(bookmark: BookmarkCreate) -> Bookmark:
    return Bookmark(id=1, **bookmark.dict())