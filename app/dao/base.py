# Класс с универсальными методами, по работе с БД
# Примеры: получение записи по id, получение всех записей, получение записей по определенному фильтру,
# удаление записи по определенному фильтру.
# Смысл: в файле base.py выносятся универсальные методы, а в файле dao.py - для каждой отдельной сущности
# прописывается индивидуальный метод под каждую конкретную задачу.

from sqlalchemy.future import select
from app.database import async_session_maker
# from app.students.models import Student


class BaseDAO:
    model = None

    @classmethod
    # async def find_all_students(cls, **filter_by):
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            students = await session.execute(query)
            return students.scalars().all()

# Метод find_all класса BaseDAO принимает неограниченное количество именованных аргументов через **filter_by