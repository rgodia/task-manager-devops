import pytest
from app.routes import app
from app.database import init_db


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test.db"

    monkeypatch.setattr(
        "app.database.DATABASE",
        test_db
    )

    init_db()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"My Task Manager" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_add_task(client):
    response = client.post(
        "/add",
        data={
            "title": "Learn Jenkins",
            "description": "Build my first CI/CD pipeline"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Learn Jenkins" in response.data


def test_complete_task(client):
    client.post(
        "/add",
        data={"title": "Learn Docker"}
    )

    client.post("/complete/1")

    response = client.get("/")

    assert b"Undo" in response.data


def test_delete_task(client):
    client.post(
        "/add",
        data={"title": "Temporary task"}
    )

    client.post("/delete/1")

    response = client.get("/")

    assert b"Temporary task" not in response.data

