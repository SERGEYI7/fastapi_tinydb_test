from typing import Union
from fastapi import FastAPI, Request
from src.users.router import routers    
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(routers)


# app.mount("/static", StaticFiles(directory="static"), name="static")

