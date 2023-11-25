import pathlib
from pprint import pprint

from pydantic import ValidationError
from tinydb import Query, TinyDB
from src.users.schemas import UserBase
from json import loads

cur_dir = pathlib.Path(__file__).parent.parent.parent
path_db = "db/Users.json"
db = TinyDB(pathlib.Path.joinpath(cur_dir, path_db), ensure_ascii=False)


def insert_new_data(name, email, phone, text, date):
    user = UserBase(name=name, email=email, phone=phone,
                    text=text, date=date)
    db.insert(loads(user.model_dump_json()))
    return True


def get_data(phone: str, email: str):
    user = Query()
    queries = db.search(user.email == email and user.phone == phone)
    return queries


def get_form_name(phone: str, email: str):
    phone = phone.replace(" ", "+")
    try:
        user = UserBase(phone=phone, email=email)
    except ValidationError as err:
        messages = dict()
        for error in err.errors():
            if error["type"] == "value_error":
                messages[error["loc"][0]] = error["msg"]
        if len(messages) > 0:
            return messages

    user = Query()
    queries = db.search((user.email == email) & (user.phone == phone))
    return list(map(lambda querie: querie["name"], queries))
