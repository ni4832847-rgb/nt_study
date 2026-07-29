from book import Book
from storage import load_books, save_books


def add_book():
    books = load_books()

    book_id = input("请输入图书编号: ").strip()
    title = input("请输入书名: ").strip()
    author = input("请输入作者: ").strip()
    category = input("请输入分类: ").strip()

    try:
        total_stock = int(input("请输入总库存: ").strip())
    except ValueError:
        print("库存必须是数字。")
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
    print("图书添加成功。")


def list_books():
    books = load_books()

    if not books:
        print("当前没有图书。")
        return

    for book in books:
        print(
            f"编号: {book.book_id} | 书名: {book.title} | 作者: {book.author} | "
            f"分类: {book.category} | 可借: {book.available_stock}/{book.total_stock}"
        )


def search_book():
    books = load_books()
    keyword = input("请输入书名关键字: ").strip()
    found = False

    for book in books:
        if keyword in book.title:
            print(
                f"编号: {book.book_id} | 书名: {book.title} | 作者: {book.author} | "
                f"分类: {book.category} | 可借: {book.available_stock}/{book.total_stock}"
            )
            found = True

    if not found:
        print("没有找到相关图书。")


def update_stock():
    books = load_books()
    book_id = input("请输入图书编号: ").strip()
    found = False

    for book in books:
        if book.book_id == book_id:
            try:
                new_stock = int(input("请输入新的总库存: ").strip())
            except ValueError:
                print("库存必须是数字。")
                return

            book.total_stock = new_stock
            book.available_stock = new_stock
            found = True
            break

    if found:
        save_books(books)
        print("库存修改成功。")
    else:
        print("没有找到该图书。")


def delete_book():
    books = load_books()
    book_id = input("请输入图书编号：").strip()
    found = False

    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            save_books(books)
            found = True
            break

    if found:
        print("删除成功")
    else:
        print("没有找到这本书")




def borrow_book():
    books = load_books()
    book_id = input("请输入图书编号: ").strip()
    found = False
    for book in books:
        if book.book_id == book_id:
            found = True

            if book.available_stock > 0:
                book.available_stock = book.available_stock - 1
                save_books(books)
                print("提示借书成功")
                break
            else:
                print("提示没有可借库存")
                break

    if not found:
        print("提示没有找到这本书")


def return_book():
    books = load_books()
    book_id = input("请输入图书编号: ").strip()
    found = False
    for book in books:
        if book.book_id == book_id:
            found = True

            if book.available_stock < book.total_stock:
                book.available_stock = book.available_stock + 1
                save_books(books)
                print("还书成功")
                break
            else:
                print("这本书没有借出")
                break

    if not found:
        print("没有找到这本书")


def low_stock_alert():
    books = load_books()
    low_stock_limit = 3
    found = False

    for book in books:
        if book.available_stock < low_stock_limit:
            print(
                f"编号: {book.book_id} | 书名: {book.title} | 作者: {book.author} | "
                f"分类: {book.category} | 可借: {book.available_stock}/{book.total_stock}"
            )
            found = True

    if not found:
        print("没有低库存图书")