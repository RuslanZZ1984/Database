from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date

# ForeignKey - внешний ключ (класс) - ссылка на значение в другой таблице, который обеспечивает целостность данных
# text - функция, позволяющая создавать текстовые фрагменты SQL напрямую в коде Python
# Text- тип данных - представляет текстовое поле в БД (строка размером 255 знаков). Можно использовать String

# Mapped, mapped_column - части SQLAlchemy, используемые для объявления сопоставления (MAPPING)
# между классами Python и структурами таблиц в базе данных.

# Создаем модель таблицы студентов
class Student(Base):
    # смотри аннотации в database
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str_null_true]
    # major_id - внешний ключ и ссылается на колонку id в таблице majors
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)

    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r}, "
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# Создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    # Количество студентов
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)
