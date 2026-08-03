from fastapi import FastAPI

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
