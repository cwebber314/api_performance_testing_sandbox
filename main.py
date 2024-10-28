"""Example app

To run:

    fastapi dev main.py
"""
from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/world")
async def world():
    return {"message": "Hello World"}

@app.get("/get100")
async def get100():
    """Between 0 - 100 ms delay
    """
    ms = random.randrange(1, 100)
    time.sleep(ms/1000)
    return {"message": "Hello World"}

@app.get("/get1000")
async def get1000():
    """Between 0 - 1000 ms delay
    """
    ms = random.randrange(1, 1000)
    time.sleep(ms/1000)
    return {"message": "Hello World"}