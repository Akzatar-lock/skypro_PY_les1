import os
import pytest
from project_api import ProjectAPI


BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://yougile.com/api-v2")
TOKEN = os.getenv("YOUGILE_TOKEN")


@pytest.fixture(scope="session")
def api():
    if not TOKEN:
        pytest.skip(
            "Не задан YOUGILE_TOKEN. "
            "Установите переменную окружения с API-ключом Yougile."
        )
    return ProjectAPI(BASE_URL, TOKEN)


@pytest.fixture
def created_project(api):
    """Создаёт проект для тестов и удаляет его после выполнения."""
    payload = {"title": "Autotest Project"}
    response = api.create_project(payload)
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]

    yield project_id

    api.delete_project(project_id)
