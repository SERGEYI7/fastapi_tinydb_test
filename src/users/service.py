import pathlib
from tinydb import Query, TinyDB
from src.users.schemas import UserBase

cur_dir = pathlib.Path.cwd()
path_db = "db/Users.json"
db = TinyDB(pathlib.Path.joinpath(cur_dir, path_db))

def insert_new_data():
    user = UserBase(email="email@email.com", phone="+79618848116",
                            text="textProbe", date="01.12.2022")
    print(user.date)
    print(user.email)
    print(user.phone)
    print(user.text)
    db.insert({"email": "mail@mail.mail",
               "phone": "+7961884816",
               "text": "qweasdzxc",
               "date": "11.04.2023",})

    return db.all()
