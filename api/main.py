from fastapi import FastAPI
from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str
    status: str = "未完成"


app = FastAPI()


tasks = [
    {"id": 1, "name": "学习 FastAPI", "status": "未完成"},
    {"id": 2, "name": "练习 pytest", "status": "未完成"},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "name": task.name,
        "status": task.status,
    }
    tasks.append(new_task)
    return new_task
