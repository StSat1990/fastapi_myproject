from fastapi import FastAPI

from news.user_news_api import news_router
from user.user_api import user_router
# Для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")


app.include_router(user_router)
app.include_router(news_router)

@app.get('/index')
async def home():
    return 'This is home page'
