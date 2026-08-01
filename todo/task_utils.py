import json


def show_tasks(tasks):
    if len(tasks) == 0:
        print("暂无任务")
    else:
        print("当前任务列表：")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} | "
                  f"截止时间：{task['deadline']} | "
                  f"状态：{task['status']}"
                  )


def count_tasks(tasks):
    return len(tasks)


def search_tasks(tasks, keyword):
    result = []
    keyword_lower = keyword.lower()

    for task in tasks:
        task_name_lower = task["name"].lower()
        if keyword_lower in task_name_lower:
            result.append(task)

    return result



def add_task(tasks, name, deadline, status, priority="普通"):
    task = {
        "name": name,
        "deadline": deadline,
        "status": status,
        "priority": priority
    }
    tasks.append(task)
    return tasks


def delete_task(tasks, index):
    real_index = index - 1

    if real_index < 0 or real_index >= len(tasks):
        return False

    tasks.pop(real_index)
    return True


def save_tasks(tasks, filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def load_tasks(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def mark_done(tasks, index):
    real_index = index - 1

    if real_index < 0 or real_index >= len(tasks):
        return False

    tasks[real_index]['status'] = '已完成'
    return True
