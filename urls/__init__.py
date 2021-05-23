from fastapi import APIRouter
from . import users
from . import orders
from . import service
from . import status
from . import auto_parts
from . import privilege


urls = APIRouter()
urls.include_router(users.app, prefix='/users', tags=['Пользователи'])
urls.include_router(orders.app, prefix='/orders', tags=['Заказы'])
urls.include_router(service.app, prefix='/service', tags=['Сервис'])
urls.include_router(status.app, prefix='/status', tags=['Статус'])
urls.include_router(auto_parts.app, prefix='/auto_parts', tags=['Автозапчасти'])
urls.include_router(privilege.app, prefix='/privilege', tags=['Привелегия'])

