# Класс с универсальными методами, по работе с БД
# Примеры: получение записи по id, получение всех записей, получение записей по определенному фильтру,
# удаление записи по определенному фильтру.
# Смысл: в файле base.py выносятся универсальные методы, а в файле dao.py - для каждой отдельной сущности
# прописывается индивидуальный метод под каждую конкретную задачу.

from sqlalchemy.future import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            students = await session.execute(query)
            return students.scalars().all()
