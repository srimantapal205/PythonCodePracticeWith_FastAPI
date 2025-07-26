
from typing import Annotated
from sqlalchemy.orm import  Session
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
import  models
from models import Todos
from  database import  SessionLocal
from starlette import  status


router = APIRouter()

# @app.get("/", status_code=status.HTTP_200_OK )
# async  def to_do():
#     return {"message": "Hello World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_depends = Annotated[Session, Depends(get_db)]

def not_found(todo_model):
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')

class TodoRequest(BaseModel):
    title :str = Field(min_length=3)
    description : str = Field(min_length=5, max_length=100)
    priority : int = Field(gt=0, lt=6)
    complete : bool



# Create a new todo item
@router.get("/todos_list",  status_code=status.HTTP_200_OK)
async  def read_all_todos(db:db_depends):
    return db.query(Todos).all()

#get single todo item by id
@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK )
async  def read_todo(db:db_depends, todo_id:int = Path(gt=0)):
    to_model = db.query(Todos).filter(todo_id == Todos.id).first()
    not_found(to_model)
    return to_model

# Create a new todo item

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async  def  create_todo(db: db_depends, todo_request :TodoRequest ):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()



@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo_item(db:db_depends,todo_request :TodoRequest, todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(todo_id == Todos.id).first()
    not_found(todo_model)
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT )
async  def delete_item(db:db_depends, todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(todo_id == Todos.id).first()
    not_found(todo_model)
    db.query(Todos).filter(todo_id == Todos.id).delete()
    db.commit()






