from enum import Enum


class PrivilegeEnum(str, Enum):
    admin = 'Администратор'
    worker = 'Работник'
    user = 'Пользователь'

