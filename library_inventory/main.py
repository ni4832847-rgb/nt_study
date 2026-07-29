from manager import (
    add_book,
    borrow_book,
    delete_book,
    list_books,
    low_stock_alert,
    return_book,
    search_book,
    update_stock,
)


def show_menu():
    print("\n==== 图书库存管理系统 ====")
    print("1. 添加图书")
    print("2. 查看所有图书")
    print("3. 搜索图书")
    print("4. 修改库存")
    print("5. 删除图书")
    print("6. 借书")
    print("7. 还书")
    print("8. 低库存提醒")
    print("0. 退出")


def main():
    while True:
        show_menu()
        choice = input("请选择功能: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            borrow_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            low_stock_alert()
        elif choice == "0":
            print("已退出系统。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()
