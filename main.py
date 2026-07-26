from fastapi import FastAPI 

best = FastAPI()


@best.get("/")
def home():
    return {"message": "hello worlds! we are changing this "}






