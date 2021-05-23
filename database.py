import sqlalchemy
import databases


# sqlite:///CarService2.db
DATABASE_URL = "sqlite:///CarService2.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
