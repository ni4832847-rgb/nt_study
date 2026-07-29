from manager import create_record, list_records, remove_record, edit_record, show_summary, search_by_date


def show_menu():
    print("=== 个人记账系统 ===")
    print("1. 新增账单")
    print("2. 查看所有账单")
    print("3. 删除账单")
    print("4. 修改账单")
    print("5. 查看收支汇总")
    print("6. 按日期查询账单")
    print("0. 退出")

def main():
    while True:
        show_menu()
        choice = input("请选择功能：").strip()

        if choice == "1":
            create_record()
        elif choice == "2":
            list_records()
        elif choice == "3":
            remove_record()
        elif choice == "4":
            edit_record()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            search_by_date()
        elif choice == "0":
            print("退出")
            break
        else:
            print("请输入正确的序号")


if __name__ == "__main__":
    main()