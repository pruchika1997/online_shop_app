from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.models.user import User as UserModel
from app.db.deps import get_db

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()
