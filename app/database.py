from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from app.config import get_db_url

DATABASE_URL = get_db_url()

# create_async_engine - создание асинхронного подлючения к БД PostgreSQL, используя драйвер asyncpg
engine = create_async_engine(DATABASE_URL)
# создание фабрики ассинхронных сессий, используя созданный движок.
# Сессии используются для выполнения транзакций в базе данных.
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Настройка аннотаций - создание кастомных шаблонов для описания колонок в SQLAlchemy
int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


# Создаем абстрактный класс, от которого наследуются все модели. Используется для миграций и
# аккумулирует информацию обо всех моделях, чтобы Alembic мог создавать миграции для синхронизации
# структуры базы данных с моделями на бэкенде.
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    # декоратор определяет имя таблицы для модели на основе имени класса с добавлением "s"
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    # Дата и время создания записи - данные берутся с сервера.
    # Mapped - аннотация, на основании передачи в неё переменной SQLAlchemy "понимает", какая должна получиться колонка.
    created_at: Mapped[created_at]
    # Текущее время сервера после обновления
    updated_at: Mapped[updated_at]
    # эти 2 колонки будут появляться в каждой создаваемой таблице