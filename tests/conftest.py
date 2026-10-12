import pytest
from fastapi.testclient import TestClient

from heroes_api.main import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(str(tmp_path / "test.db"))
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def harbour_council(client):
    response = client.post(
        "/clients",
        json={
            "name": "Brindlemouth Harbour Council",
            "plan": "Max",
            "seats": 10,
            "contact_email": "dispatch@harbour-council.example",
        },
    )
    return response.json()
