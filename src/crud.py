from sqlalchemy.orm import Session
from src import models, schemas


class Crud:

    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def create_user(db: Session, user: schemas.UserCreate):
        db_user = models.User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def create_article(db: Session, article: schemas.ArticleCreate, user_id: int):
        db_article = models.Article(**article.model_dump(), owner_id=user_id)
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
