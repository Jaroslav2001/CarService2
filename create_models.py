import sqlalchemy
from database import metadata, DATABASE_URL, database
from models import *
from emun import PrivilegeEnum
import asyncio


async def with_connect(func):
    async with database:
        await func()


async def create():
    await User.objects.create(
        name=user, password=password, email=email, privilege=PrivilegeEnum.admin.value
    )


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)

    user = input('Введите логин: ')
    password = input('Введите пароль: ')
    email = input('Введите почту: ')
    asyncio.run(with_connect(create))
