import sqlalchemy
import databases


# sqlite:///CarService2.db
# mysql://root:root@127.0.0.1/test_auto
DATABASE_URL = "sqlite:///CarService2.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
