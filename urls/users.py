from fastapi import APIRouter
import models
from typing import Optional
from schemas.users import *
from func import check_users


app = APIRouter()


@app.get('/')
async def api(id_user: Optional[int] = None, user: Optional[str] = None):
    if not(id_user is None):
        return await models.User.objects.filter(id=id_user).get_or_none()
    if user is None:
        return await models.User.objects.all()
    return await models.User.objects.filter(name=user).get_or_none()


@app.post('/')
async def api(user: UserFormPost):
    privilege = await models.Privilege.objects.get(name='Пользователь')
    try:
        user_result = await models.User.objects.create(
            name=user.login,
            password=user.password,
            email=user.email,
            privilege=privilege
        )
    except:
        return {"error": "user"}
    else:
        return {"result": user_result}


@app.put('/')
async def api(user: UserFromPut):
    user_get = await check_users(user=user)
    if 'error' in user_get:
        return user_get
    user_result = await models.User.objects.filter(name=user.login).update(
        name=user.login,
        password=user.new_password,
        email=user.new_email
    )
    return {"result": user_result}


@app.delete('/')
async def api(user: UserForm):
    user_get = await check_users(user=user)
    if 'error' in user_get:
        return user_get

    user_result = await models.User.objects.delete(name=user.login)
    return {"result": user_result}


@app.patch('/')
async def api(login: str, admin: UserForm, privilege_name: str):
    admin_get = await check_users(user=admin, privilege=1)
    if 'error' in admin_get:
        return admin_get
    privilege = await models.Privilege.objects.get(name=privilege_name)
    result = await models.User.objects.filter(name=login).update(privilege=privilege)
    return {'result': result}

