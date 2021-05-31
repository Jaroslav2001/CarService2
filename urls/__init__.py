from fastapi import APIRouter
from . import users
from . import orders
from . import service
from . import auto_parts


urls = APIRouter()
urls.include_router(users.app, prefix='/users', tags=['Пользователи'])
urls.include_router(orders.app, prefix='/orders', tags=['Заказы'])
urls.include_router(service.app, prefix='/service', tags=['Сервис'])
urls.include_router(auto_parts.app, prefix='/auto_parts', tags=['Автозапчасти'])

