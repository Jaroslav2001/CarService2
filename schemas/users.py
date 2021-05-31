from pydantic import BaseModel


class UserFormPost(BaseModel):
    login: str
    password: str
    email: str


class UserForm(BaseModel):
    login: str
    password: str


class UserFromPut(UserForm):
    new_password: str
    new_email: str
