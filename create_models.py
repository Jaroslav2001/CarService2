import sqlalchemy
from database import metadata, DATABASE_URL, database
from models import *
import asyncio


async def with_connect(func):
    async with database:
        await func()


async def create():
    await Status.objects.bulk_create([
        Status(name='Заказ автовапчасти'),
        Status(name='Ремот автомобиля'),
        Status(name='Отремонтирован'),
        Status(name='Ищем ремонтника автомобиля'),
        Status(name='Ждём автомобиль'),
        Status(name='Заказ выполнен')
    ])

    admin = await Privilege.objects.create(name='Администратор')
    await Privilege.objects.create(name='Рабочий')
    await Privilege.objects.create(name='Пользователь')

    await Users.objects.create(
        name=user, password=password, email=email, privilege=admin
    )


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)

    user = input('Введите логин: ')
    password = input('Введите пароль: ')
    email = input('Введите почту: ')
    asyncio.run(with_connect(create))
