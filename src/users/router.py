from fastapi import APIRouter, Request
from src.users.service import insert_new_data
from starlette.templating import Jinja2Templates
from src.users.schemas import UserBase
from pydantic import BaseModel

routers = APIRouter(include_in_schema=False)


@routers.get("/")
def index(request: Request):
    print(insert_new_data())
    return {"Hello": "World"}


@routers.post("/user/")
async def index(user: UserBase):
    # Todo Здесь нужно использовать логику сделаную в service для запросов в бд
    return {"email": user.email,
            "phone": user.phone,
            "text": user.text,
            "date": user.date}