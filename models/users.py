import ormar
import os
from database import database, metadata
from .privilege import Privilege


class Users(ormar.Model):
    class Meta:
        tablename = "users"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, unique=True, nullable=False)
    password: str = ormar.String(
        max_length=128,
        nullable=False,
        encrypt_secret=os.urandom(20).hex(),
        encrypt_backend=ormar.EncryptBackends.HASH
    )
    email: str = ormar.String(max_length=100)
    privilege: Privilege = ormar.ForeignKey(Privilege)
