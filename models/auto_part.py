import ormar
from decimal import Decimal
from database import database, metadata


class AutoPart(ormar.Model):
    class Meta:
        tablename = "auto_part"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200, unique=True, nullable=False)
    price: Decimal = ormar.Decimal(max_digits=11, decimal_places=2)
    description: str = ormar.Text()
