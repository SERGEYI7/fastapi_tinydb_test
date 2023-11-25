from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic_core import PydanticCustomError
import re


class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    text: str
    date: str

    @field_validator("phone")
    def phone_validation(cls, v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise PydanticCustomError("value_error", "Number phone invalid")
        return v

    @field_validator("date")
    def date_validation(cls, v):
        regex = r"^(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d$"
        if v and not re.search(regex, v, re.I):
            raise PydanticCustomError("value_error", "Date invalid")
        return v
