from enum import Enum


class StatusEnum(str, Enum):
    search_worker = 'Ищем ремонтника'
    wait_auto = 'Ждём автомобиль'
    order_auto_parts = 'Заказ автозапчасти'
    repairs_auto = 'Ремот автомобиля'
    renovated = 'Отремонтирован'
    order_completed = 'Заказ выполнен'
