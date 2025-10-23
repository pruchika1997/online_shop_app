from fastapi import APIRouter
from app.schemas.user import User
from app.models.user import UserModel

router = APIRouter()

users_db: list[UserModel] = []

@router.post("/", response_model=User)
def create_user(user: User):
    users_db.append(UserModel(**user.dict()))
    return user

@router.get("/", response_model=list[User])
def list_users():
    return users_db