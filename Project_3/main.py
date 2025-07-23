
from fastapi import FastAPI
from starlette import  status
import  models
from  database import  engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# @app.get("/", status_code=status.HTTP_200_OK )
# async  def to_do():
#     return {"message": "Hello World"}