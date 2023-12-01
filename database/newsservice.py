from .models import UserNews, NewsPhoto
from datetime import datetime

from database import get_db

# Добавления новости
def add_news_db(user_id, news_text):
    db = next(get_db())

    # Создать обьект для базы данных
    news = UserNews(user_id=user_id,
                        news_text=news_text,
                        publish_date=datetime.now())
    db.add(news)
    db.commit()

    return 'Успешно добавлено'


# Добавить фото к новости
def add_news_photo_db(news_id, news_photo):
    db = next(get_db())

    news_photo = NewsPhoto(news_id=news_id, photo_path=news_photo)

    db.add(news_photo)
    db.commit()

    return f'Фотография загружена id - {news_photo.id}'

#Получить фото новости
def get_news_photo_db():
    db = next(get_db())

    news_photo = db.query(NewsPhoto).all()

    return news_photo

# Изменить новость
def edit_news_db(news_id, user_id, new_text):
    db = next(get_db())

    exact_news = db.query(UserNews).filter_by(id=news_id, user_id=user_id).first()

    if exact_news:
        exact_news.news_text = new_text
        db.commit()

        return 'Новость успешно изменена'
    else:
        return False


# Удалить новость
def delete_news_db(news_id):
    db = next(get_db())

    delete_news = db.query(UserNews).filter_by(id=news_id).first()
    delete_news_photo = db.query(NewsPhoto).filter_by(news_id=news_id).first()

    if delete_news:
        db.delete(*delete_news_photo)
        db.commit()

        db.delete(delete_news)
        db.commit()

        return "Новость успешно удалена"
    else:
        return False


#Получить все новости
def get_all_news_db():
    db = next(get_db())

    all_news = db.query(UserNews).all()
    return all_news


#Получить определенную новость
def get_exact_news_db(news_id):
    db = next(get_db())

    exact_news = db.query(UserNews).filter_by(news_id=news_id).first()

    if exact_news:
        return exact_news
    else:
        return 'Error'
