from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int

app = FastAPI()

@app.post("/register")
def register(user:User):
    return{"message":f"Welcome{user.name}"}