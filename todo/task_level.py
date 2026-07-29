task1 = input("请输入今天第一个任务:")
task2 = input("请输入今天第二个任务：")
task3 = input("请输入今天第三个任务：")
tasks = []
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

print(f"今天的学习列表是{tasks}")

do_task = int(input("你今天完成了几项任务："))

if do_task == 0:
    print("今天还没开始，加油")
elif do_task == 1:
    print("已经完成1个，继续推进")
elif do_task == 2:
    print("完成一大半了，很不错")
elif do_task == 3:
    print("全部完成了，今天很棒")
else:
    print("输入不正确")