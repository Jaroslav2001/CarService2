import ormar
from typing import List
from database import database, metadata

from .user import User
from .service import Service
from .auto_part import AutoPart
from typing import Optional
from datetime import date
from emun import StatusEnum


class Order(ormar.Model):
    class Meta:
        tablename = "order"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    status: str = ormar.String(max_length=20, choices=list(StatusEnum))
    date: date = ormar.Date()
    service: List[Service] = ormar.ManyToMany(Service)
    auto_parts: Optional[List[AutoPart]] = ormar.ManyToMany(AutoPart)
    description: str = ormar.Text()
