from fastapi import FastAPI
from typing import List 
from starlette.middleware.cors import CORSMiddleware  
from db import session 
from model import ArticleTable, Article, PostArticle, PutArticle, User, UserTable 
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/articles")
def read_articles():
    articles = session.query(ArticleTable).all()
    return articles
 
@app.get("/articles/{article_id}")
def read_article(article_id: int):
    article = session.query(ArticleTable).filter(ArticleTable.id == article_id).first()
    return article

@app.post("/articles")
async def create_article(article:PostArticle):
    article_db = ArticleTable()
    article_db.name = article.name
    article_db.title = article.title
    article_db.content = article.content
    article_db.date = datetime.now()
    session.add(article_db)
    session.commit()
    return article_db

@app.put("/articles")
async def update_articles(article:PutArticle):
    article_db = session.query(ArticleTable).filter(ArticleTable.id == article.id).first()
    article_db.title = article.title
    article_db.content = article.content
    article_db.date = datetime.now()
    session.commit()
    return article_db

@app.post("/articles/{article_id}")
async def delete_article(article_id: int):
    article_db = session.query(ArticleTable).filter(ArticleTable.id == article_id).first()
    session.delete(article_db)
    session.commit()
    return article_db 

@app.post("/user")
async def create_user(user: User):
    user_db = UserTable()
    user_db.name = user.name
    user_db.password = user.password
    session.add(user_db)
    session.commit()
    return user_db

@app.get("/users")
async def login_check(name: str, password: str):
    user_db = session.query(UserTable).filter(UserTable.name == name).filter(UserTable.password == password).first()
    return user_db

@app.get("/user/")
async def login_check():
    user_db = session.query(UserTable).all()
    return user_db