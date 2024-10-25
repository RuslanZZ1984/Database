# DAO - Data Access Object (объект доступа к данным).
# Содержаться индивидуальные функции, относящиеся к конкретной сущности.
# Сущность - студенты и функции БД, которые относятся исключительно к студентам
# Другие названия возможные - core.py либо service.py.

# from app.dao.base import BaseDAO
# from app.students.models import Student
#
#
# class StudentDAO(BaseDAO):
#     model = Student

# from sqlalchemy import select
# from app.students.models import Student
# # from app.students.schemas import SStudent
# from app.database import async_session_maker
#
#
# class StudentDAO:
#     @classmethod
#     async def find_all_students(cls):
#         async with async_session_maker() as session:
#             query = select(Student)
#             students = await session.execute(query)
#             return students.scalars().all()

from app.dao.base import BaseDAO
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student
