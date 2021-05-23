from fastapi import APIRouter
import models
from typing import Optional

app = APIRouter()


@app.get('/')
async def api(name: Optional[str] = None):
    if name is None:
        return await models.AutoParts.objects.all()
    return await models.AutoParts.objects.filter(name=name).get_or_none()


@app.post('/')
async def api(users: models.Users):
    new_users = await users.save()
    return new_users
