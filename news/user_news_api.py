from fastapi import APIRouter, UploadFile, Body

from news import PublicNewsValidator, EditNewsValidator

from database.newsservice import add_news_db, add_news_photo_db, edit_news_db, delete_news_db, get_all_news_db, \
    get_exact_news_db

news_router = APIRouter(prefix='/user_news', tags=['Работа с новостями'])


# Запрос на публикацию новости
@news_router.post('/public_news')
async def public_news(data: PublicNewsValidator):
    result = add_news_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! Not Found'}

# Запрос на изменения текста новости
@news_router.put('/change_news')
async def change_news(data: EditNewsValidator):
    result = edit_news_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! not found'}


# Запрос на удаления новости
@news_router.delete('/delete_news')
async def delete_news(news_id: int):
    result = delete_news_db(news_id)

    if result:
        return {'message': result, 'status': 'Deleted'}
    else:
        return {'message': 'Post not found'}

# Запрос на получения всех новостей
@news_router.get('/get_all_news')
async def get_all_news():
    result = get_all_news_db()

    return {'message': result}

# Запрос для добавления фото к новости
@news_router.post('/add_photo')
async def add_photo(news_id: int = Body(),
                    photo_file: UploadFile = None
                    ):
    photo_path = f'/media/{photo_file.filename}'
    try:
        # Сохранения фотографии в папку media
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

        # Сохранения ссылки к фотографии в базу
        result = add_news_photo_db(post_id=news_id, post_photo=photo_path)

    except Exception as error:
        result = error

    return {'message': result}


# Получить определенную новость
@news_router.get('/get_exact_news')
async def get_exact_news(news_id: int):
    result = get_exact_news_db(news_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}