import json

try:
    with open('tasks.json','r',encoding='utf-8') as f:
        tasks = json.load(f)

    if len(tasks) == 0:
        print("暂无任务")
    else:
        print("任务列表")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}:{task['name']}"
                  f"截止日期:{task['deadline']}"
                  f"状态:{task['status']}")

except FileNotFoundError:
    print("任务文件不存在：请先保存任务.")
except json.JSONDecodeError:
    print("任务文件格式错误，请检查 tasks.json.")