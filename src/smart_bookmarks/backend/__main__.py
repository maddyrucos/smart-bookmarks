import uvicorn

uvicorn.run(
    "smart_bookmarks.backend.main:app", 
    host="0.0.0.0", 
    port=8000, 
    reload=True
)