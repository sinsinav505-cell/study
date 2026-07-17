from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"message": "Hello,World!"}

@app.post("/register")

def register(user:dict):
    return {
        "message":f"Welcome{user['name']}"
        }