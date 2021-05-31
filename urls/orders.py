from fastapi import APIRouter
import models
from typing import Optional

app = APIRouter()


@app.get('/')
async def api(name: Optional[str] = None):
    if name is None:
        return await models.Order.objects.all()
    return await models.Order.objects.filter(name=name).get_or_none()


@app.post('/')
async def api(orders: models.Order):
    orders = await orders.save()
    return orders
