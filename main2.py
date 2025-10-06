from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# class Users(BaseModel):
#     firstName: str
#     lastName:str
#     age:int
    

items = []


@app.get("/")
def index():
    return {"Hello", "world"}


@app.post("/item")
def create_item(item: str):
    items.append(item)
    return items


    
