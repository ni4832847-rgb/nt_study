name = input("请输入任务名称：")
deadline = input("请输入截止日期：")
status = input("请输入任务状态：")

task = {
    "name":name,
    "deadline":deadline,
    "status":status
}

print("任务详情：")
print(f"任务名称：{task['name']}")
print(f"截止日期：{task['deadline']}")
print(f"任务状态:{task['status']}")