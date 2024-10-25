# Теория
# В FastAPI Router - инструмент, который помогает организовать и группировать маршруты (пути) web-приложения.
# Router позволяет собрать функции, отвечающие за разные URL-адреса в одно место, а затем добавить в основное приложени
# Router позволяет сгруппировать функции, которые взаимодействуют с конкретной сущностью (студенты, преподаватели и пр.)


# APIRouter используется для создания маршрутов (routes) для API
from fastapi import APIRouter, Depends
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent

# from app.students.schemas import SStudent

# APIRouter - создает экземпляр класса
# prefix='/students' - префикс всех маршрутов. Маршруты, добавленные к этому роуту, будут начинаться с /students
# tags=['Работа со студентами'] - Добавляет тег к роутеру, который будет использоваться в документации Swagger для группировки и описания маршрутов.
router = APIRouter(prefix='/students', tags=['Работа со студентами'])


# # Это работает без response_model
# @router.get("/", summary="получить всех студентов") #, response_model=list[SStudent])
# async def get_all_students():
#     return await StudentDAO.find_all()

@router.get('/', summary="ПОлучить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list:  # list[SStudent]: - не работает SStudent
    return await StudentDAO.find_all(**request_body.to_dict())
# Параметры в документации выводятся с app.students.rb


# @router.get("/", summary="Получить всех студентов", response_model=list[SStudent])
# async def get_all_students():
#     # создание ассинхронной сессии для работы с БД
#     return await StudentDAO.find_all_students()
