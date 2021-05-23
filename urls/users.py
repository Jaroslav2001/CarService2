from fastapi import APIRouter
import models
from typing import Optional
from schemas.users import *


app = APIRouter()


@app.get('/')
async def api(id_user: Optional[int] = None, user: Optional[str] = None):
    if not(id_user is None):
        return await models.Users.objects.filter(id=id_user).get_or_none()
    if user is None:
        return await models.Users.objects.all()
    return await models.Users.objects.filter(name=user).get_or_none()


@app.post('/')
async def api(user: UserFormPost):
    privilege = await models.Privilege.objects.get(name='Пользователь')
    user_result = await models.Users.objects.create(
        name=user.login,
        password=user.password,
        email=user.email,
        privilege=privilege
    )
    return user_result


@app.put('/')
async def api(user: UserFromPut):
    user_get = await models.Users.objects.filter(name=user.login).get_or_none()
    if user_get is None:
        return None
    user_form = models.Users(name=user.login, password=user.password, email='123')
    if user.password != user_form.password:
        return {'password': 'error'}
    user_result = await models.Users.objects.update(
        name=user.login,
        password=user.new_password,
        email=user.new_email
    )
    return user_result


@app.delete('/')
async def api(user: UserFormDelete):
    user_get = await models.Users.objects.filter(name=user.login).get_or_none()
    if user_get is None:
        return None
    user_form = models.Users(name=user.login, password=user.password, email='123')
    if user.password != user_form.password:
        return {'password': 'error'}
    user_result = await models.Users.objects.delete(name=user.login)
    return user_result
