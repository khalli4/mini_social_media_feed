"""Routes for user operations"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate

router = APIRouter()


@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Create a new user including the password field
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password  # make sure your User model has this column
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
