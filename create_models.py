import sqlalchemy
from database import metadata, DATABASE_URL
from models import *


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)
