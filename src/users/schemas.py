from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserBase(BaseModel):
    email: EmailStr
    phone: str
    text: str
    date: str

    @field_validator("phone")
    def phone_validation(cls, v):
        # phone = v.phone.get("phone") #  <-- This line needs to be removed.
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Phone Number Invalid.")
        return v

    @field_validator("date")
    def date_validation(cls, v):
        # phone = v.phone.get("phone") #  <-- This line needs to be removed.
        regex = r"^(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Date Invalid.")
        return v


# m = UserBase(email="primer@prime.com", phone="+79618848116", text="text primer", date="11.12.2023")
