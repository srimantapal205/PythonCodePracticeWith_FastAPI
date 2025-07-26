from typing import Annotated
from fastapi import  APIRouter,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import  Users
from passlib.context import  CryptContext
from fastapi.security import  OAuth2PasswordRequestForm




router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    role : str
    is_active: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_depends = Annotated[Session, Depends(get_db)]
"""
{
  "username": "Learn_FastAPI",
  "email": "lfa@test.com",
  "first_name": "Learn",
  "last_name": "FastApi",
  "hashed_password": "Password",
  "role": "admin",
  "is_active": true
}
"""
@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async  def create_user(db : db_depends,create_user_request: CreateUserRequest):
    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role=create_user_request.role,
        hashed_password= bcrypt_context.hash(create_user_request.hashed_password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token")
async  def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_depends):
    return  form_data.username




# @router.get("userList")
# async def get_user():
#
