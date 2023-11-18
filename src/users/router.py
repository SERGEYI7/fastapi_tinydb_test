from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
import pydantic

routers = APIRouter(include_in_schema=False)


@routers.get("/")
def index(request: Request):
    return {"Hello": "World"}


@routers.post("/")
async def index(request: Request):
    form = await request.form()
    email = form.get("email")
    return {"": ""}