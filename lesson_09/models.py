from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from db import Base


class SoftDeleteMixin:
    """Примесь для мягкого удаления."""
    deleted_at = Column(DateTime, nullable=True, default=None)

    def soft_delete(self):
        # Используем современный метод вместо устаревшего utcnow()
        self.deleted_at = datetime.now(timezone.utc)

    def restore(self):
        self.deleted_at = None

    @classmethod
    def active(cls):
        """Возвращает только неудалённые записи."""
        return cls.query.filter(cls.deleted_at.is_(None))


class Student(Base, SoftDeleteMixin):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    level = Column(String(50))
    education_form = Column(String(50))
    subject_id = Column(Integer)


class Teacher(Base, SoftDeleteMixin):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True)
    email = Column(String(100))
    group_id = Column(Integer)


class Subject(Base, SoftDeleteMixin):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(100))
