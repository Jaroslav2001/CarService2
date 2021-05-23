import ormar
from database import database, metadata


class Status(ormar.Model):
    class Meta:
        tablename = "status"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200, unique=True, nullable=False)
    description: str = ormar.Text(default='')
