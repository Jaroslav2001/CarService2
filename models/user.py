import ormar
from database import database, metadata
from emun import PrivilegeEnum
from setting import secret


class User(ormar.Model):
    class Meta:
        tablename = "user"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, unique=True, nullable=False)
    password: str = ormar.String(
        max_length=128,
        nullable=False,
        encrypt_secret=secret,
        encrypt_backend=ormar.EncryptBackends.HASH
    )
    email: str = ormar.String(max_length=100)
    privilege: str = ormar.String(max_length=20, choices=list(PrivilegeEnum))
