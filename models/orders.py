import ormar
from typing import List
from database import database, metadata

from .users import Users
from .service import Service
from .auto_parts import AutoParts
from .status import Status


class Orders(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: Users = ormar.ForeignKey(Users)
    status: Status = ormar.ForeignKey(Status)
    service: List[Service] = ormar.ManyToMany(Service)
    auto_parts: List[AutoParts] = ormar.ManyToMany(AutoParts)
    description: str = ormar.Text()
