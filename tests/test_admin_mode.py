from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_students_can_view_activities_without_login():
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_requires_teacher_authentication():
    response = client.post("/activities/Chess Club/signup?email=novo@mergington.edu")
    assert response.status_code == 403
    assert response.json()["detail"] == "Autenticação de professor necessária"


def test_teacher_login_and_admin_signup_work():
    login = client.post(
        "/login",
        json={"username": "teacher", "password": "mhs-admin"},
    )
    assert login.status_code == 200
    assert login.json()["role"] == "teacher"

    response = client.post(
        "/activities/Chess Club/signup?email=novo@mergington.edu&username=teacher&password=mhs-admin"
    )
    assert response.status_code == 200
    assert "novo@mergington.edu" in client.get("/activities").json()["Chess Club"]["participants"]


def test_teacher_can_unregister_student():
    response = client.delete(
        "/activities/Chess Club/unregister?email=novo@mergington.edu&username=teacher&password=mhs-admin"
    )
    assert response.status_code == 200
    assert "novo@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]
