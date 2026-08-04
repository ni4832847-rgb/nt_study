from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str
    status: str = "未完成"


class TaskUpdate(BaseModel):
    name: str
    status: str


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


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int,task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = task_update.name
            task["status"] = task_update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "name": task.name,
        "status": task.status,
    }
    tasks.append(new_task)
    return new_task
