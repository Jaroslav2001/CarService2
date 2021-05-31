import models
from schemas.users import *
from setting import get_hash


async def check_users(user: UserForm, privilege: int = 3):
    user_get = await models.Users.objects.filter(name=user.login).get_or_none()
    if user_get is None:
        return {'error': 'user'}
    if user_get.password != get_hash(user.password):
        return {'error': 'password'}
    if user_get.privilege.id > privilege:
        return {'error': 'privilege'}
    return {'result': user_get}
