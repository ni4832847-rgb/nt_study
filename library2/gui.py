from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

try:
    from .book import Book
    from .storage import load_books, save_books, load_records, save_records
except ImportError:
    from book import Book
    from storage import load_books, save_books, load_records, save_records


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图书管理系统")
        self.root.geometry("1100x720")
        self.root.minsize(960, 640)

        self.fields = {}
        self._build_ui()
        self.refresh_books()

    def _build_ui(self):
        top_frame = ttk.LabelFrame(self.root, text="图书信息")
        top_frame.pack(fill="x", padx=12, pady=10)

        labels = [
            ("book_id", "图书编号", 0, 0),
            ("title", "书名", 0, 2),
            ("author", "作者", 0, 4),
            ("category", "分类", 1, 0),
            ("total_stock", "总库存", 1, 2),
            ("borrower", "借阅人", 1, 4),
            ("keyword", "搜索关键字", 2, 0),
        ]

        for key, text, row, col in labels:
            ttk.Label(top_frame, text=text).grid(
                row=row, column=col, padx=6, pady=6, sticky="e"
            )
            entry = ttk.Entry(top_frame, width=26)
            if key == "keyword":
                entry.grid(row=row, column=col + 1, columnspan=3, padx=6, pady=6, sticky="we")
            else:
                entry.grid(row=row, column=col + 1, padx=6, pady=6, sticky="w")
            self.fields[key] = entry

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=12, pady=4)

        buttons = [
            ("新增", self.add_book),
            ("修改库存", self.update_stock),
            ("删除", self.delete_book),
            ("借书", self.borrow_book),
            ("还书", self.return_book),
            ("搜索", self.search_book),
            ("低库存", self.low_stock_alert),
            ("借阅记录", self.show_borrow_records),
            ("刷新", self.refresh_books),
        ]

        for index, (text, command) in enumerate(buttons):
            ttk.Button(button_frame, text=text, command=command).grid(
                row=0, column=index, padx=4, pady=4
            )

        list_frame = ttk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=12, pady=10)

        columns = ("book_id", "title", "author", "category", "total_stock", "available_stock")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=16)

        headings = {
            "book_id": "编号",
            "title": "书名",
            "author": "作者",
            "category": "分类",
            "total_stock": "总库存",
            "available_stock": "可借库存",
        }
        widths = {
            "book_id": 110,
            "title": 220,
            "author": 160,
            "category": 140,
            "total_stock": 100,
            "available_stock": 100,
        }

        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="center")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.fill_form_from_selection)

        self.status_var = tk.StringVar(value="就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, anchor="w")
        status_bar.pack(fill="x", padx=12, pady=(0, 10))

    def _get(self, name):
        return self.fields[name].get().strip()

    def _set_status(self, text):
        self.status_var.set(text)

    def _clear_form(self):
        for entry in self.fields.values():
            entry.delete(0, tk.END)

    def _selected_book_id(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection[0], "values")
            if values:
                return values[0]
        return self._get("book_id")

    def _books(self):
        return load_books()

    def refresh_books(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        books = self._books()
        for book in books:
            self.tree.insert(
                "",
                "end",
                values=(
                    book.book_id,
                    book.title,
                    book.author,
                    book.category,
                    book.total_stock,
                    book.available_stock,
                ),
            )

        self._set_status(f"已加载 {len(books)} 本图书")

    def fill_form_from_selection(self, _event=None):
        selection = self.tree.selection()
        if not selection:
            return

        values = self.tree.item(selection[0], "values")
        if not values:
            return

        for key, value in zip(
            ["book_id", "title", "author", "category", "total_stock"],
            values[:5],
        ):
            self.fields[key].delete(0, tk.END)
            self.fields[key].insert(0, value)

    def add_book(self):
        book_id = self._get("book_id")
        title = self._get("title")
        author = self._get("author")
        category = self._get("category")
        total_stock_text = self._get("total_stock")

        if not all([book_id, title, author, category, total_stock_text]):
            messagebox.showwarning("提示", "请把图书信息填完整")
            return

        try:
            total_stock = int(total_stock_text)
        except ValueError:
            messagebox.showerror("错误", "总库存必须是整数")
            return

        if total_stock < 0:
            messagebox.showerror("错误", "总库存不能小于 0")
            return

        books = self._books()
        if any(book.book_id == book_id for book in books):
            messagebox.showwarning("提示", "图书编号已存在")
            return

        books.append(
            Book(
                book_id=book_id,
                title=title,
                author=author,
                category=category,
                total_stock=total_stock,
                available_stock=total_stock,
            )
        )
        save_books(books)
        self.refresh_books()
        self._set_status("新增成功")
        messagebox.showinfo("成功", "新增成功")

    def update_stock(self):
        book_id = self._selected_book_id()
        if not book_id:
            messagebox.showwarning("提示", "请选择一本图书，或者先填写图书编号")
            return

        total_stock_text = self._get("total_stock")
        if not total_stock_text:
            messagebox.showwarning("提示", "请输入新的总库存")
            return

        try:
            new_total = int(total_stock_text)
        except ValueError:
            messagebox.showerror("错误", "总库存必须是整数")
            return

        if new_total < 0:
            messagebox.showerror("错误", "总库存不能小于 0")
            return

        books = self._books()
        for book in books:
            if book.book_id == book_id:
                borrowed_count = book.total_stock - book.available_stock
                if new_total < borrowed_count:
                    messagebox.showerror("错误", f"新库存不能少于已借出数量：{borrowed_count}")
                    return
                book.total_stock = new_total
                book.available_stock = new_total - borrowed_count
                save_books(books)
                self.refresh_books()
                self._set_status("库存修改成功")
                messagebox.showinfo("成功", "库存修改成功")
                return

        messagebox.showwarning("提示", "没有找到这本图书")

    def delete_book(self):
        book_id = self._selected_book_id()
        if not book_id:
            messagebox.showwarning("提示", "请选择一本图书，或者先填写图书编号")
            return

        if not messagebox.askyesno("确认", f"确定删除图书 {book_id} 吗？"):
            return

        books = self._books()
        new_books = [book for book in books if book.book_id != book_id]
        if len(new_books) == len(books):
            messagebox.showwarning("提示", "没有找到这本图书")
            return

        save_books(new_books)
        self.refresh_books()
        self._set_status("删除成功")
        messagebox.showinfo("成功", "删除成功")

    def borrow_book(self):
        book_id = self._selected_book_id()
        borrower = self._get("borrower")
        if not book_id or not borrower:
            messagebox.showwarning("提示", "请选择图书并填写借阅人")
            return

        books = self._books()
        for book in books:
            if book.book_id == book_id:
                if book.available_stock <= 0:
                    messagebox.showwarning("提示", "没有可借库存")
                    return

                book.available_stock -= 1
                save_books(books)

                records = load_records()
                records.append(
                    {
                        "book_id": book_id,
                        "book_title": book.title,
                        "borrower": borrower,
                        "borrowed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "returned_at": None,
                        "returned": False,
                    }
                )
                save_records(records)
                self.refresh_books()
                self._set_status("借书成功")
                messagebox.showinfo("成功", "借书成功")
                return

        messagebox.showwarning("提示", "没有找到这本图书")

    def return_book(self):
        book_id = self._selected_book_id()
        borrower = self._get("borrower")
        if not book_id or not borrower:
            messagebox.showwarning("提示", "请选择图书并填写借阅人")
            return

        books = self._books()
        for book in books:
            if book.book_id == book_id:
                records = load_records()
                for record in records:
                    if (
                        record["book_id"] == book_id
                        and record["borrower"] == borrower
                        and not record["returned"]
                    ):
                        record["returned"] = True
                        record["returned_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        book.available_stock += 1
                        save_records(records)
                        save_books(books)
                        self.refresh_books()
                        self._set_status("还书成功")
                        messagebox.showinfo("成功", "还书成功")
                        return

                messagebox.showwarning("提示", "没有找到对应的借阅记录")
                return

        messagebox.showwarning("提示", "没有找到这本图书")

    def search_book(self):
        keyword = self._get("keyword")
        if not keyword:
            messagebox.showwarning("提示", "请输入搜索关键字")
            return

        books = self._books()
        matched = [
            book
            for book in books
            if keyword in book.book_id
            or keyword in book.title
            or keyword in book.author
            or keyword in book.category
        ]
        self._show_book_window(f"搜索结果 - {keyword}", matched)

    def low_stock_alert(self):
        books = self._books()
        matched = [book for book in books if book.available_stock < 3]
        self._show_book_window("低库存图书", matched)

    def show_borrow_records(self):
        records = load_records()
        window = tk.Toplevel(self.root)
        window.title("借阅记录")
        window.geometry("980x500")

        columns = ("book_id", "book_title", "borrower", "borrowed_at", "returned_at", "status")
        tree = ttk.Treeview(window, columns=columns, show="headings")
        headings = {
            "book_id": "编号",
            "book_title": "书名",
            "borrower": "借阅人",
            "borrowed_at": "借出时间",
            "returned_at": "还书时间",
            "status": "状态",
        }
        widths = {
            "book_id": 90,
            "book_title": 210,
            "borrower": 120,
            "borrowed_at": 180,
            "returned_at": 180,
            "status": 90,
        }

        for column in columns:
            tree.heading(column, text=headings[column])
            tree.column(column, width=widths[column], anchor="center")

        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for record in records:
            tree.insert(
                "",
                "end",
                values=(
                    record["book_id"],
                    record.get("book_title", "未知"),
                    record["borrower"],
                    record.get("borrowed_at") or "未知",
                    record.get("returned_at") or "未归还",
                    "已归还" if record["returned"] else "借阅中",
                ),
            )

    def _show_book_window(self, title, books):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("900x400")

        columns = ("book_id", "title", "author", "category", "total_stock", "available_stock")
        tree = ttk.Treeview(window, columns=columns, show="headings")
        headings = {
            "book_id": "编号",
            "title": "书名",
            "author": "作者",
            "category": "分类",
            "total_stock": "总库存",
            "available_stock": "可借库存",
        }

        for column in columns:
            tree.heading(column, text=headings[column])
            tree.column(column, width=130, anchor="center")

        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for book in books:
            tree.insert(
                "",
                "end",
                values=(
                    book.book_id,
                    book.title,
                    book.author,
                    book.category,
                    book.total_stock,
                    book.available_stock,
                ),
            )

        if not books:
            messagebox.showinfo("提示", "没有找到匹配结果")


def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
