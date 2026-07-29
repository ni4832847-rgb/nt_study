from task_utils import show_tasks, add_task, delete_task, save_tasks, load_tasks, mark_done

FILENAME = "tasks.json"


def main():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n任务管理系统")
        print("1. 查看任务")
        print("2. 新增任务")
        print("3. 删除任务")
        print("4. 标记完成")
        print("5. 保存并退出")

        choice = input("请选择操作：")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            name = input("请输入任务名称：")
            deadline = input("请输入截止日期：")
            status = input("请输入任务状态：")
            add_task(tasks, name, deadline, status)
            print("任务已新增")

        elif choice == "3":
            show_tasks(tasks)

            try:
                index = int(input("请输入要删除的任务序号："))
            except ValueError:
                print("请输入正确的数字序号")
                continue

            result = delete_task(tasks, index)

            if result:
                print("任务已删除")
            else:
                print("序号无效，删除失败")


        elif choice == "4":
            show_tasks(tasks)

            try:
                index = int(input("请输入要标记完成的任务序号："))
            except ValueError:
                print("请输入正确的数字序号")
                continue

            result = mark_done(tasks, index)

            if result:
                print("任务已标记完成")
            else:
                print("序号无效，操作失败")

        elif choice == "5":
            save_tasks(tasks, FILENAME)
            print("任务已保存，再见")
            break


        else:
            print("输入无效，请重新选择")


if __name__ == "__main__":
    main()
