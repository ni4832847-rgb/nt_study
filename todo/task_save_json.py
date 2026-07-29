import json

tasks = []

for i in range(1,4):
    name = input(f"请输入第{i}个任务名称：")
    deadline = input(f"请输入第{i}个截止日期：")
    status = input(f"请输入第{i}个任务状态:")

    task = {
        "name":name,
        "deadline":deadline,
        "status":status
    }

    tasks.append(task)

with open("tasks.json","w", encoding='utf-8') as f:
    json.dump(tasks,f, ensure_ascii=False, indent=2)

print("任务已保存到 tasks.json")
