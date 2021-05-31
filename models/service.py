import ormar
from decimal import Decimal
from database import database, metadata
from datetime import date


class Service(ormar.Model):
    class Meta:
        tablename = "service"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200, nullable=False)
    price: Decimal = ormar.Decimal(max_digits=11, decimal_places=2)
    description: str = ormar.Text()
    visibility: bool = ormar.Boolean()
    date: date = ormar.Date()
