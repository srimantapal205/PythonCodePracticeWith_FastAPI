from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Todos
from database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags = ['Admin']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return  db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()





"""
 {
    "id": 1,
    "priority": 5,
    "complete": false,
    "title": "Learn HTML",
    "description": "For Fullstack ",
    "owner_id": 1
  },
  {
    "id": 2,
    "priority": 5,
    "complete": false,
    "title": "Learn DSA",
    "description": "Start learning DSA",
    "owner_id": 1
  },
  {
    "id": 3,
    "priority": 2,
    "complete": false,
    "title": "Task_1",
    "description": "Task 1 need to work one",
    "owner_id": 2
  },
  {
    "id": 4,
    "priority": 3,
    "complete": false,
    "title": "Task_2",
    "description": "Task 2 needs to work on one",
    "owner_id": 2
  },
  {
    "id": 5,
    "priority": 4,
    "complete": false,
    "title": "Task_3",
    "description": "Task 3 needs to work on one",
    "owner_id": 2
  }
"""


