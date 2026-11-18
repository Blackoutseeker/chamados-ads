from app import app
import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_status_and_json(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.get_json() == {"mensagem": "API de chamados em funcionamento"}
