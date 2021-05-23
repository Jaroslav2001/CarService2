import sqlalchemy
import databases


DATABASE_URL = "sqlite:///CarService2.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
