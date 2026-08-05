from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator


def validate_task_name(value):
    if value.strip() == "":
        raise ValueError("Task name must not be blank")
    return value


class TaskCreate(BaseModel):
    name: str = Field(min_length=1)
    status: str = "未完成"

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value):
        return validate_task_name(value)

class TaskUpdate(BaseModel):
    name: str = Field(min_length=1)
    status: str


    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value):
        return validate_task_name(value)


class Task(BaseModel):
    id: int
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


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int,task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = task_update.name
            task["status"] = task_update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model= Task ,status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "name": task.name,
        "status": task.status,
    }
    tasks.append(new_task)
    return new_task
