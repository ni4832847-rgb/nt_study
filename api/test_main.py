from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


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

    assert response.status_code == 200
    assert response.json() == {"id": 3, "name": "测试创建任务","status": "未完成"}


def test_create_task_with_default_status():
    response = client.post(
        "/tasks",
        json={"name": "默认状态任务"}
    )

    assert response.status_code == 200
    assert response.json() == {"id": 4, "name": "默认状态任务", "status": "未完成"}