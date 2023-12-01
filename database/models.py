from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Создаем таблицу пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


# Таблица новостей
class UserNews(Base):
    __tablename__ = 'user_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    news_text = Column(String)
    news_photo = Column(String)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy="subquery")

# Таблица фотографий
class NewsPhoto(Base):
    __tablename__ = 'news_photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    news_id = Column(Integer, ForeignKey("user_news.id"))
    news_photo = Column(String)

    post_fk = relationship(UserNews, lazy='subquery')

