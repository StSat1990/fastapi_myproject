from pydantic import BaseModel

# Валидатор публикации поста
class PublicNewsValidator(BaseModel):
    user_id: int
    news_text: str

# Валидатор для изменения текста к посту
class EditNewsValidator(BaseModel):
    news_id: int
    new_text: str
    user_id: int
