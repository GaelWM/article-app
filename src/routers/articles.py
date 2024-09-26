from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.crud import Crud as crud
from src.schemas import Article, ArticleCreate

router = APIRouter()

@router.post("/articles/", response_model=Article)
def create_article(article: ArticleCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_article(db, article, user_id)
