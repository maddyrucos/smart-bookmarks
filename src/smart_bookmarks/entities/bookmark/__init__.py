from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

class BookmarkCreate(BaseModel):
    url: str
    title: str
    description: str | None = None

class Bookmark(BookmarkCreate):
    id: int


class BookmarkORM(declarative_base()):
    __tablename__ = "bookmarks"

    id: int = Column(Integer, primary_key=True)
    url: str = Column(String, nullable=False)
    title: str = Column(String, nullable=False)
    description: str | None = Column(Text, nullable=True)

    class Config:
        orm_mode = True