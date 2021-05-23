import ormar
from database import database, metadata


class Users(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=500)
    email: str = ormar.String(max_length=100)
