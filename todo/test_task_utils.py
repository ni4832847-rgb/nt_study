import os
import tempfile

from task_utils import count_tasks, add_task, delete_task, save_tasks, load_tasks, mark_done, search_tasks


def test_count_tasks_empty():
    tasks = []
    assert count_tasks(tasks) == 0


def test_count_tasks_two():
    tasks = [
        {"name": "学习python", "deadline": "2026-07-23", "status": "完成"},
        {"name": "学习git", "deadline": "2026-07-23", "status": "完成"}
    ]
    assert count_tasks(tasks) == 2


def test_add_task_to_empty_list():
    tasks = []

    result = add_task(tasks, "学习python", "2026-07-23", "未完成")

    assert len(result) == 1
    assert result[0]["deadline"] == "2026-07-23"
    assert result[0]['name'] == "学习python"
    assert result[0]['status'] == "未完成"
    assert result[0]['priority'] == "普通"

def test_add_task_with_priority():
    tasks = []

    result = add_task(tasks, "学习python", "2026-07-23", "未完成", priority="高")

    assert len(result) == 1
    assert result[0]["deadline"] == "2026-07-23"
    assert result[0]['name'] == "学习python"
    assert result[0]['status'] == "未完成"
    assert result[0]['priority'] == "高"


def test_add_task_to_existing_list():
    tasks = [
        {"name": "学习python", "deadline": "2026-07-23", "status": "未完成"},
    ]

    result = add_task(tasks, "学习python", "2026-07-23", "未完成")
    assert len(result) == 2
    assert result[1]["name"] == "学习python"


def test_delete_first_task():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"},
        {"name": "练习 Git", "deadline": "2026-07-28", "status": "未完成"}
    ]

    result = delete_task(tasks, 1)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["name"] == "练习 Git"


def test_delete_second_task():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"},
        {"name": "练习 Git", "deadline": "2026-07-28", "status": "未完成"}
    ]

    result = delete_task(tasks, 2)
    assert len(tasks) == 1
    assert tasks[0]['name'] == "学习 Python"


def test_delete_invalid_task_index_too_large():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"}
    ]

    result = delete_task(tasks, 10)

    assert result is False
    assert len(tasks) == 1


def test_delete_invalid_task_index_zero():
    tasks = [
        {"name": "练习 Git", "deadline": "2026-07-28", "status": "未完成"}
    ]

    result = delete_task(tasks, 0)

    assert result is False
    assert len(tasks) == 1


def test_save_and_load_tasks():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"}
    ]

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    filename = temp_file.name
    temp_file.close()

    try:
        save_tasks(tasks, filename)
        result = load_tasks(filename)

        assert result == tasks
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def test_mark_done_success():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"}
    ]

    result = mark_done(tasks, 1)
    assert result is True
    assert tasks[0]['status'] == '已完成'


def test_mark_done_invalid_index():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-07-27", "status": "未完成"}
    ]

    result = mark_done(tasks, 10)

    assert result is False
    assert tasks[0]['status'] == '未完成'

def test_search_tasks_by_name():
    tasks = [
        {"name": "学习 python", "deadline": "2026-08-02", "status": "未完成"},
        {"name": "练习 Git", "deadline": "2026-08-03", "status": "未完成"},
    ]

    result = search_tasks(tasks, "python")

    assert len(result) == 1
    assert result[0]["name"] == "学习 python"


def test_search_tasks_ignore_case():
    tasks = [
        {"name": "学习 Python", "deadline": "2026-08-02", "status": "未完成"},
        {"name": "练习 Git", "deadline": "2026-08-03", "status": "未完成"},
    ]

    result = search_tasks(tasks, "python")

    assert len(result) == 1
    assert result[0]["name"] == "学习 Python"
