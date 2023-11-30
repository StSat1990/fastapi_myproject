from pydantic import BaseModel

# Валидатор публикации поста
class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str

# Валидатор для изменения текста к посту
class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
    user_id: int
