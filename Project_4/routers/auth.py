from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import  APIRouter,Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import  Users
from passlib.context import  CryptContext
from fastapi.security import  OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError





router = APIRouter(
    prefix='/auth',
    tags = ['auth']
)

SECRET_KEY = "ed379e7fb5b96087273864545fa15105b6119e776ff29e8f38c0f5c91b2f0af5"
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
outh2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')



class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    role : str
    is_active: bool

class Token(BaseModel):
    access_token : str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_depends = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return  False
    if not bcrypt_context.verify(password, user.hashed_password):
        return  False
    return  user

def create_access_token(username: str, user_id: int, role:str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role':role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires.timestamp()})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async  def get_current_user(token: Annotated[str, Depends(outh2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username : str = payload.get('sub')
        user_id : int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or  user_id is None:
            raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')

        return  {'username': username, 'id': user_id, 'user_role': user_role}

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')




"""
def authenticate_user(username: str, password: str, db: Session):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires.timestamp()})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


"""


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


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_depends):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return  {'access_token': token, 'token_type': 'bearer' }

"""
@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_depends):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return JSONResponse(content={"error": "Failed to authenticate"}, status_code=status.HTTP_401_UNAUTHORIZED)
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return JSONResponse(content={"access_token": token, "token_type": "bearer"}, 

"""
# @router.get("userList")
# async def get_user():
#
