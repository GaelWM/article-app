from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class User(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class ArticleCreate(BaseModel):
    title: str
    content: str

class Article(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True
