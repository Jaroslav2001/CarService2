from pydantic import BaseModel
from decimal import Decimal


class ServiceFormPost(BaseModel):
    name: str
    price: Decimal
    description: str
    visibility: bool
