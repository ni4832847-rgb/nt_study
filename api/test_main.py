import pytest
from fastapi.testclient import TestClient

from api.main import app, tasks


client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    tasks.extend(
        [
            {"id": 1, "name": "学习 FastAPI", "status": "未完成"},
            {"id": 2, "name": "练习 pytest", "status": "未完成"},
        ]
    )


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "学习 FastAPI", "status": "未完成"},
        {"id": 2, "name": "练习 pytest", "status": "未完成"},
    ]


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "学习 FastAPI", "status": "未完成"}


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_create_task():
    response = client.post("/tasks", json={"name": "测试创建任务", "status": "未完成"},)

    assert response.status_code == 201
    assert response.json() == {"id": 3, "name": "测试创建任务","status": "未完成"}


def test_create_task_with_default_status():
    response = client.post(
        "/tasks",
        json={"name": "默认状态任务"}
    )

    assert response.status_code == 201
    assert response.json() == {"id": 3, "name": "默认状态任务", "status": "未完成"}


def test_update_task():
    response = client.put(
        "/tasks/1",
        json={"name": "学习 FastAPI", "status": "已完成"},
    )

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "学习 FastAPI", "status": "已完成"}


def test_update_missing_task():
    response = client.put(
        "/tasks/999",
        json={"name": "不存在的任务", "status": "已完成"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_delete_task():
    response = client.delete("/tasks/2")

    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted"}

    list_response = client.get("/tasks")
    assert list_response.json() == [
        {"id": 1, "name": "学习 FastAPI", "status": "未完成"},
    ]


def test_delete_missing_task():
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}









