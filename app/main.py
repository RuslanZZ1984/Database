from enum import Enum

from fastapi import FastAPI

from utils import json_to_dict_list
import os
from typing import Optional, List

from students.models import Student
import requests

app = FastAPI()

# Получаем путь к директории текущего скрипта
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Переходим на уровень выше
# parent_dir = os.path.dirname(script_dir)
#
# # Получаем путь к JSON
# path_to_json = os.path.join(parent_dir, 'students.json')г

# Свернутая запись
path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')


@app.get('/')
def home_page():
    return {'message': 'Home page'}


# @app.get("/students")
# def get_all_students(course: Optional[int] = None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student["course"] == course:
#                 return_list.append(student)
#         return return_list

@app.get("/student")
def get_student_from_param_id(student_id: int) -> Student:
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get('')
@app.get("/students/{student_id}")
def get_all_students(student_id: Optional[int] = 1):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student


# Запуск http://127.0.0.1:8000/students/1?enrollment_year=2019?major=Психология
@app.get("/students/{course}")
def get_all_students(course: Optional[int] = None, major: Optional[str] = None,
                     enrollment_year: Optional[int] = 2018) -> List[Student]:
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student['course'] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


# Наследуясь от str и Enum - создаем перечисления, где каждый член вляется строкой
class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"
    engineering = "Инженерия"
    languages = "Языки"
