import pytest
from sqlalchemy.orm import sessionmaker

from db import engine, Base

TestingSessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)


@pytest.fixture(scope="function")
def db_session():
    """
    Создаёт соединение и сессию.
    После теста откатывает все изменения.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    Base.metadata.create_all(bind=connection)

    yield session

    session.close()
    transaction.rollback()   # откат всех изменений
    connection.close()
