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

print("任务列表")
for index, task in enumerate(tasks,start=1):
    print(f"{index}. {task['name']}"
          f"截止日期{task['deadline']}"
          f"状态{task['status']}")