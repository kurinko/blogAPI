from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from db import Base
from db import ENGINE
from datetime import datetime

class ArticleTable(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    title = Column(String(100))
    content = Column(String(200))
    date = Column(DateTime)

class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    password = Column(String(100))

class Article(BaseModel):
    id: int
    name: str
    title: str
    content: str
    date: datetime

class PostArticle(BaseModel):
    name: str
    title: str
    content: str   

class PutArticle(BaseModel):
    id: int
    title: str
    content: str

class User(BaseModel):
    name: str
    password: str


def main():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()
