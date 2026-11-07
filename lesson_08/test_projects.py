import uuid

import pytest


class TestCreateProject:
    """Тесты для [POST] /api-v2/projects"""

    def test_create_project_positive(self, api):
        unique_title = f"New Project {uuid.uuid4().hex[:6]}"
        payload = {
            "title": unique_title,
        }
        response = api.create_project(payload)

        assert response.status_code == 201
        body = response.json()
        assert "id" in body
        project_id = body["id"]

        # Проверяем, что проект действительно создался с нужным названием
        # через дополнительный GET-запрос
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == unique_title

    @pytest.mark.parametrize("payload", [
        {},
        {"title": ""},
        {"title": 12345},
    ])
    def test_create_project_negative(self, api, payload):
        response = api.create_project(payload)
        assert response.status_code in (400, 422)


class TestGetProject:
    """Тесты для [GET] /api-v2/projects/{id}"""

    def test_get_project_positive(self, api, created_project):
        response = api.get_project(created_project)

        assert response.status_code == 200
        body = response.json()
        assert body["id"] == created_project
        assert "title" in body

    def test_get_project_negative_not_found(self, api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.get_project(fake_id)
        assert response.status_code == 404

    def test_get_project_negative_invalid_id(self, api):
        response = api.get_project("invalid-id")
        assert response.status_code in (400, 404)


class TestUpdateProject:
    """Тесты для [PUT] /api-v2/projects/{id}"""

    def test_update_project_positive(self, api, created_project):
        unique_title = f"Updated Title {uuid.uuid4().hex[:6]}"
        payload = {"title": unique_title}

        response = api.update_project(created_project, payload)
        assert response.status_code == 200

        updated = api.get_project(created_project)
        assert updated.json()["title"] == unique_title

    def test_update_project_negative_not_found(self, api):
        payload = {"title": "Whatever"}
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.update_project(fake_id, payload)
        assert response.status_code == 404

    def test_update_project_negative_invalid_body(self, api, created_project):
        payload = {"title": ""}
        response = api.update_project(created_project, payload)
        assert response.status_code in (400, 422)
