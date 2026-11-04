import uvicorn

from smart_bookmarks.config import settings

uvicorn.run(
    "smart_bookmarks.backend.main:app", 
    host=settings.backend.host, 
    port=settings.backend.port, 
    reload=settings.backend.reload
)