from fastapi import APIRouter
import models
from typing import Optional

app = APIRouter()


@app.get('/')
async def api(name: Optional[str] = None):
    if name is None:
        return await models.Orders.objects.all()
    return await models.Orders.objects.filter(name=name).get_or_none()


@app.post('/')
async def api(orders: models.Orders):
    orders = await orders.save()
    return orders
