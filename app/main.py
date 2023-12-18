from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import List
from random import randrange
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from sqlalchemy.orm import Session
from . import models, schema, utils
from .database import engine, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='sannhtet899', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}
