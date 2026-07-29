import json

with open('tasks.json', 'r',encoding='utf-8') as f:
    tasks = json.load(f)

if len(tasks) == 0:
    print("暂无任务")
else:
    print("任务列表:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} |"
              f"截止日期{task['deadline']} |"
              f"状态{task['status']} |"
        )