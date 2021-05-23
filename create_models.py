import sqlalchemy
from database import metadata, DATABASE_URL, database
from models import *
import asyncio


async def with_connect(func):
    async with database:
        await func()


async def create_status():
    await Status.objects.bulk_create([
        Status(name='Заказ автовапчасти'),
        Status(name='Ремот автомобиля'),
        Status(name='Отремонтирован'),
        Status(name='Ищем ремонтника автомобиля'),
        Status(name='Ждём автомобиль'),
        Status(name='Заказ выполнен')
    ])


async def create_privilege():
    await Privilege.objects.bulk_create([
        Privilege(name='Администратор'),
        Privilege(name='Рабочий'),
        Privilege(name='Пользователь')
    ])


async def create_user():
    user = input('Введите логин')
    password = input('Введите пароль')
    email = input('Введите почту')

    await Users.objects.create(
        name=user, password=password, email=email, privilege=0
    )


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)
    for func in [create_status, create_privilege, create_user]:
        asyncio.run(with_connect(func))
