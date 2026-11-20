from sqlalchemy import select

from models import Student, Subject, Teacher


# ------------------------------------------------------------------
# ТЕСТЫ ДЛЯ STUDENT
# ------------------------------------------------------------------
def test_create_student(db_session):
    student = Student(
        user_id=9991,
        level="Бакалавриат",
        education_form="Очная",
        subject_id=1,
    )
    db_session.add(student)
    db_session.commit()

    saved = db_session.execute(
        select(Student).where(Student.user_id == 9991)
    ).scalar_one()

    assert saved is not None
    assert saved.level == "Бакалавриат"
    assert saved.user_id == 9991


def test_update_student(db_session):
    student = Student(
        user_id=9992,
        level="1 курс",
        education_form="Бюджет",
        subject_id=1,
    )
    db_session.add(student)
    db_session.commit()

    student.level = "2 курс"
    db_session.commit()

    updated = db_session.execute(
        select(Student).where(Student.user_id == 9992)
    ).scalar_one()

    assert updated.level == "2 курс"


def test_delete_student(db_session):
    student = Student(
        user_id=9993,
        level="Магистратура",
        education_form="Платная",
        subject_id=1,
    )
    db_session.add(student)
    db_session.commit()

    student.soft_delete()
    db_session.commit()

    deleted = db_session.execute(
        select(Student).where(Student.user_id == 9993)
    ).scalar_one()

    assert deleted is not None
    assert deleted.deleted_at is not None


# ------------------------------------------------------------------
# ТЕСТЫ ДЛЯ TEACHER
# ------------------------------------------------------------------
def test_create_teacher(db_session):
    teacher = Teacher(
        teacher_id=8881,
        email="test_teacher@mail.ru",
        group_id=1,
    )
    db_session.add(teacher)
    db_session.commit()

    saved = db_session.execute(
        select(Teacher).where(Teacher.teacher_id == 8881)
    ).scalar_one()

    assert saved is not None
    assert saved.email == "test_teacher@mail.ru"


def test_update_teacher(db_session):
    teacher = Teacher(
        teacher_id=8882,
        email="old_email@mail.ru",
        group_id=1,
    )
    db_session.add(teacher)
    db_session.commit()

    teacher.email = "new_email@mail.ru"
    db_session.commit()

    updated = db_session.execute(
        select(Teacher).where(Teacher.teacher_id == 8882)
    ).scalar_one()

    assert updated.email == "new_email@mail.ru"


def test_delete_teacher(db_session):
    teacher = Teacher(
        teacher_id=8883,
        email="delete_me@mail.ru",
        group_id=1,
    )
    db_session.add(teacher)
    db_session.commit()

    teacher.soft_delete()
    db_session.commit()

    deleted = db_session.execute(
        select(Teacher).where(Teacher.teacher_id == 8883)
    ).scalar_one()

    assert deleted is not None
    assert deleted.deleted_at is not None


# ------------------------------------------------------------------
# ТЕСТЫ ДЛЯ SUBJECT
# ------------------------------------------------------------------
def test_create_subject(db_session):
    subject = Subject(
        subject_id=7771,
        subject_title="Математика",
    )
    db_session.add(subject)
    db_session.commit()

    saved = db_session.execute(
        select(Subject).where(Subject.subject_title == "Математика")
    ).scalar_one()

    assert saved is not None
    assert saved.subject_title == "Математика"


def test_update_subject(db_session):
    subject = Subject(
        subject_id=7772,
        subject_title="Физика",
    )
    db_session.add(subject)
    db_session.commit()

    subject.subject_title = "Квантовая физика"
    db_session.commit()

    updated = db_session.execute(
        select(Subject).where(Subject.subject_id == 7772)
    ).scalar_one()

    assert updated.subject_title == "Квантовая физика"


def test_delete_subject(db_session):
    subject = Subject(
        subject_id=7773,
        subject_title="Удаляемый Предмет",
    )
    db_session.add(subject)
    db_session.commit()

    subject.soft_delete()
    db_session.commit()

    deleted = db_session.execute(
        select(Subject).where(Subject.subject_id == 7773)
    ).scalar_one()

    assert deleted is not None
    assert deleted.deleted_at is not None
