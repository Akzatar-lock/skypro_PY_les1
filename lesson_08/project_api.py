import requests


class ProjectAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _url(self, path: str = "") -> str:
        return f"{self.base_url}/projects{path}"

    def create_project(self, payload: dict) -> requests.Response:
        return requests.post(
            self._url(), json=payload, headers=self.headers
        )

    def get_project(self, project_id: str) -> requests.Response:
        return requests.get(
            self._url(f"/{project_id}"), headers=self.headers
        )

    def update_project(
        self, project_id: str, payload: dict
    ) -> requests.Response:
        return requests.put(
            self._url(f"/{project_id}"),
            json=payload,
            headers=self.headers
        )

    def delete_project(self, project_id: str) -> requests.Response:
        return requests.delete(
            self._url(f"/{project_id}"), headers=self.headers
        )
