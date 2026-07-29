import json
import sqlite3
from pathlib import Path

from book import Book


BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "library.db"
BOOK_JSON_FILE = BASE_DIR / "book.json"
RECORD_JSON_FILE = BASE_DIR / "borrow_records.json"


def _connect():
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def _initialize_database():
    with _connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT NOT NULL,
                total_stock INTEGER NOT NULL,
                available_stock INTEGER NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS borrow_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id TEXT NOT NULL,
                book_title TEXT NOT NULL,
                borrower TEXT NOT NULL,
                borrowed_at TEXT,
                returned_at TEXT,
                returned INTEGER NOT NULL DEFAULT 0
            )
            """
        )

    _migrate_json_data()


def _migrate_json_data():
    with _connect() as connection:
        book_count = connection.execute(
            "SELECT COUNT(*) FROM books"
        ).fetchone()[0]
        record_count = connection.execute(
            "SELECT COUNT(*) FROM borrow_records"
        ).fetchone()[0]

        if book_count == 0 and BOOK_JSON_FILE.exists():
            data = json.loads(BOOK_JSON_FILE.read_text(encoding="utf-8"))
            connection.executemany(
                """
                INSERT OR IGNORE INTO books
                (book_id, title, author, category, total_stock, available_stock)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["category"],
                        item["total_stock"],
                        item["available_stock"],
                    )
                    for item in data
                ],
            )

        if record_count == 0 and RECORD_JSON_FILE.exists():
            data = json.loads(RECORD_JSON_FILE.read_text(encoding="utf-8"))
            connection.executemany(
                """
                INSERT INTO borrow_records
                (book_id, book_title, borrower, borrowed_at, returned_at, returned)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        item["book_id"],
                        item.get("book_title", "未知"),
                        item["borrower"],
                        item.get("borrowed_at"),
                        item.get("returned_at"),
                        int(item.get("returned", False)),
                    )
                    for item in data
                ],
            )


def load_books():
    _initialize_database()
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT book_id, title, author, category, total_stock, available_stock
            FROM books
            ORDER BY book_id
            """
        ).fetchall()
    return [Book.from_dict(dict(row)) for row in rows]


def save_books(books):
    _initialize_database()
    with _connect() as connection:
        connection.execute("DELETE FROM books")
        connection.executemany(
            """
            INSERT INTO books
            (book_id, title, author, category, total_stock, available_stock)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    book.book_id,
                    book.title,
                    book.author,
                    book.category,
                    book.total_stock,
                    book.available_stock,
                )
                for book in books
            ],
        )


def load_records():
    _initialize_database()
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT book_id, book_title, borrower, borrowed_at, returned_at, returned
            FROM borrow_records
            ORDER BY id
            """
        ).fetchall()

    records = []
    for row in rows:
        record = dict(row)
        record["returned"] = bool(record["returned"])
        records.append(record)
    return records


def save_records(records):
    _initialize_database()
    with _connect() as connection:
        connection.execute("DELETE FROM borrow_records")
        connection.executemany(
            """
            INSERT INTO borrow_records
            (book_id, book_title, borrower, borrowed_at, returned_at, returned)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    record["book_id"],
                    record.get("book_title", "未知"),
                    record["borrower"],
                    record.get("borrowed_at"),
                    record.get("returned_at"),
                    int(record.get("returned", False)),
                )
                for record in records
            ],
        )
