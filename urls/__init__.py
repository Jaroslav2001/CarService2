from fastapi import APIRouter
from . import users


urls = APIRouter()
urls.include_router(users.app, prefix='/users')
