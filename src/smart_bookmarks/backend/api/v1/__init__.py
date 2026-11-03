from fastapi import APIRouter
from .bookmarks import bookmarks_router

v1_router = APIRouter(prefix="/v1", tags=["v1"])
v1_router.include_router(bookmarks_router)