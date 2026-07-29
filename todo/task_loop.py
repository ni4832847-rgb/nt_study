tasks = []

for i in range(1,6):
    task = input(f"请输入第{i}个任务：")
    tasks.append(task)

print("今天的任务列表:")

for index, task in enumerate(tasks,start=1):
    print(f"{index}:{task}")