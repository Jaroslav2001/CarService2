from fastapi import APIRouter
import models

app = APIRouter()


@app.get('/')
async def api():
    users = await models.Users.objects.all()
    return users
