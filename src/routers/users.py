from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.crud import Crud as crud
from src.schemas import User, UserCreate

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
