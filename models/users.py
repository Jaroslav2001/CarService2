import ormar
from database import database, metadata
from .privilege import Privilege


class Users(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, unique=True, nullable=False)
    password: str = ormar.String(max_length=500, nullable=False)
    email: str = ormar.String(max_length=100)
    privilege: Privilege = ormar.ForeignKey(Privilege)
