from pydantic import BaseModel


class UserFormPost(BaseModel):
    login: str
    password: str
    email: str


class UserFormDelete(BaseModel):
    login: str
    password: str


class UserFromPut(UserFormDelete):
    new_password: str
    new_email: str