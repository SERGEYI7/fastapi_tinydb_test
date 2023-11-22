from typing import Union
from fastapi import FastAPI, Request
from src.users.router import routers
import uvicorn
from tinydb import TinyDB
import pathlib
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# app.mount("/static", StaticFiles(directory="static"), name="static")

