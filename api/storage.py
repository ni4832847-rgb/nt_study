import json
from pathlib import Path

TASKS_FILE = Path("api/tasks.json")

DEFAULT_TASKS = [
    {"id": 1, "name": "学习 FastAPI", "status": "未完成"},
    {"id": 2, "name": "练习 pytest", "status": "未完成"},
]


def save_tasks():
    TASKS_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_tasks():
    if not TASKS_FILE.exists():
        TASKS_FILE.write_text(
            json.dumps(DEFAULT_TASKS, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return json.loads(TASKS_FILE.read_text(encoding="utf-8"))


tasks = load_tasks()
