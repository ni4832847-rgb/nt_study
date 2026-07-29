def show_tasks(tasks):
    if len(tasks) == 0:
        print("暂无任务")
    else:
        print("任务列表：")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}. {task}")


tasks = []
for i in range(1, 4):
    task = input(f"请输入第{i}个任务：")
    tasks.append(task)

show_tasks(tasks)