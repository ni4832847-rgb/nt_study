from datetime import datetime

from book import Book
from storage import load_books, save_books, load_records, save_records


def _print_book(book):
    print(
        f"编号：{book.book_id}\n"
        f"名称：{book.title}\n"
        f"作者：{book.author}\n"
        f"类别：{book.category}\n"
        f"总库存：{book.total_stock}\n"
        f"可借库存：{book.available_stock}\n"
    )


def add_book():
    books = load_books()

    book_id = input("请输入图书编号：").strip()
    if any(book.book_id == book_id for book in books):
        print("图书编号已存在")
        return

    title = input("请输入图书名称：").strip()
    author = input("请输入作者名称：").strip()
    category = input("请输入图书类别：").strip()

    try:
        total_stock = int(input("请输入总库存：").strip())
    except ValueError:
        print("库存必须是数字")
        return

    if total_stock < 0:
        print("库存不能小于 0")
        return

    new_book = Book(
        book_id=book_id,
        title=title,
        author=author,
        category=category,
        total_stock=total_stock,
        available_stock=total_stock,
    )
    books.append(new_book)
    save_books(books)
    print("添加成功")


def list_books():
    books = load_books()
    if not books:
        print("当前没有图书")
        return

    for book in books:
        _print_book(book)


def search_book():
    books = load_books()
    keyword = input("请输入关键词：").strip()
    found = False

    for book in books:
        searchable_fields = (
            book.book_id,
            book.title,
            book.author,
            book.category,
        )
        if any(keyword in field for field in searchable_fields):
            _print_book(book)
            found = True

    if not found:
        print("没有找到相关书籍")


def update_stock():
    books = load_books()
    book_id = input("请输入图书编号：").strip()

    for book in books:
        if book.book_id == book_id:
            try:
                new_stock = int(input("请输入新的总库存：").strip())
            except ValueError:
                print("库存必须是数字")
                return

            if new_stock < 0:
                print("库存不能小于 0")
                return

            borrowed_count = book.total_stock - book.available_stock
            if new_stock < borrowed_count:
                print(f"新的总库存不能少于已借出数量：{borrowed_count}")
                return

            book.total_stock = new_stock
            book.available_stock = new_stock - borrowed_count
            save_books(books)
            print("库存修改成功")
            return

    print("没有找到该图书")


def delete_book():
    books = load_books()
    book_id = input("请输入图书编号：").strip()

    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            save_books(books)
            print("删除成功")
            return

    print("没有找到这本书")


def borrow_book():
    books = load_books()
    book_id = input("请输入图书编号：").strip()
    borrower = input("请输入借阅人姓名：").strip()

    for book in books:
        if book.book_id == book_id:
            if book.available_stock > 0:
                book.available_stock -= 1
                save_books(books)
                records = load_records()
                records.append({
                    "book_id": book_id,
                    "book_title": book.title,
                    "borrower": borrower,
                    "borrowed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "returned_at": None,
                    "returned": False,
                })
                save_records(records)
                print("借书成功")
            else:
                print("没有可借库存")
            return

    print("没有找到这本书")


def return_book():
    books = load_books()
    book_id = input("请输入图书编号：").strip()
    borrower = input("请输入借阅人姓名：").strip()

    for book in books:
        if book.book_id == book_id:
            if book.available_stock < book.total_stock:
                records = load_records()
                for record in records:
                    if (
                        record["book_id"] == book_id
                        and record["borrower"] == borrower
                        and not record["returned"]
                    ):
                        record["returned"] = True
                        record["returned_at"] = datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                        save_records(records)
                        book.available_stock += 1
                        save_books(books)
                        print("还书成功")
                        return
                print("没有找到该借阅记录")
                return
            print("这本书没有借出")
            return

    print("没有找到这本书")


def list_borrow_records():
    records = load_records()
    if not records:
        print("当前没有借阅记录")
        return

    for record in records:
        status = "已归还" if record["returned"] else "借阅中"
        returned_at = record.get("returned_at") or "尚未归还"
        print(
            f"图书编号：{record['book_id']}\n"
            f"图书名称：{record.get('book_title', '未知')}\n"
            f"借阅人：{record['borrower']}\n"
            f"借书时间：{record.get('borrowed_at', '未知')}\n"
            f"还书时间：{returned_at}\n"
            f"状态：{status}\n"
        )


def low_stock_alert():
    books = load_books()
    low_stock_limit = 3
    found = False

    for book in books:
        if book.available_stock < low_stock_limit:
            print("低库存提醒")
            _print_book(book)
            found = True

    if not found:
        print("没有低库存书籍")
