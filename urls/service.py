from fastapi import APIRouter
import models
from schemas.service import *
from schemas.users import *
from typing import Optional
from func import check_users
from datetime import date

app = APIRouter()


@app.get('/')
async def api(id_service: Optional[int] = None, name: Optional[str] = None):
    if not(id_service is None):
        return await models.Service.objects.filter(id=id_service).get_or_none()
    if name is None:
        return await models.Service.objects.all()
    return await models.Service.objects.filter(name=name).get_or_none()


@app.post('/')
async def api(service: ServiceFormPost, user: UserForm):
    user_get = await check_users(user=user, privilege=2)
    if 'error' is user_get:
        return user_get

    service_result = await models.Service.objects.create(
        name=service.name,
        price=service.price,
        description=service.description,
        visibility=service.visibility,
        date=date.today()
    )
    return {"result": service_result}


@app.patch('/')
async def api(id_service: int, user: UserForm):
    user_get = await check_users(user=user, privilege=2)
    if 'error' is user_get:
        return user_get
    service = await models.Service.objects.filter(id=id_service).get_or_none()
    if service is None:
        return {'error': 'not service'}
    await models.Service.objects.filter(id=id_service).update(visibility=not service.visibility)
    return await models.Service.objects.filter(id=id_service).get_or_none()


@app.delete('/')
async def api(id_service: int, user: UserForm):
    user_get = await check_users(user=user, privilege=1)
    if 'error' is user_get:
        return user_get
    service = await models.Service.objects.filter(id=id_service).get_or_none()
    if service is None:
        return {'error': 'not service'}
    return models.Service.objects.filter(id=id_service).delete()
