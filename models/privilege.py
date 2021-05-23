import ormar
from database import database, metadata


class Privilege(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200, unique=True, nullable=False)
    description: str = ormar.Text(default='')
