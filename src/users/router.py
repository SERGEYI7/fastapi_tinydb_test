from fastapi import APIRouter, Request
from src.users.service import insert_new_data, get_form_name
from src.users.schemas import UserBase

routers = APIRouter(include_in_schema=False)


@routers.get("/")
def index(request: Request):
    return {"Hello": "World"}


@routers.post("/get_form")
async def index(email=None, phone=None):
    return_missing = {}
    if email is None:
        return_missing["email"] = "missing argument email"
    if phone is None:
        return_missing["phone"] = "missing argument phone"
    if len(return_missing) > 0:
        return return_missing
    return get_form_name(email=email, phone=phone)


@routers.post("/set_users")
async def add_user(user: UserBase):
    result = insert_new_data(name=user.name,
                             email=user.email,
                             phone=user.phone,
                             text=user.text,
                             date=user.date)
    return {"result": result}
