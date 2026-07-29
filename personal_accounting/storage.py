import sqlite3
from pathlib import Path
from record import Record

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "accounting.db"


def _connect():
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    return connection

def _initialize_database():
    with _connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_type TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                record_date TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def load_records():
    _initialize_database()


    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT record_id, record_type, amount, category, description, record_date, created_at
            FROM records
            ORDER BY record_date DESC, record_id DESC
            """
        ).fetchall()

    return [Record.from_dict(dict(row)) for row in rows]


def add_record(record):
    _initialize_database()


    with _connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO records
            (record_type, amount, category, description, record_date, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                record.record_type,
                record.amount,
                record.category,
                record.description,
                record.record_date,
                record.created_at,
            ),
        )

    return cursor.lastrowid


def delete_record(record_id):
    _initialize_database()


    with _connect() as connection:
        cursor = connection.execute(
            "DELETE FROM records WHERE record_id = ?",
            (record_id,),
        )
    return cursor.rowcount



def update_record(record):
    _initialize_database()


    with _connect() as connection:
        cursor = connection.execute(
            """
            UPDATE records
            SET record_type = ?, amount = ?, category = ?, description = ?, record_date = ?
            WHERE record_id = ?""",
            (
                record.record_type,
                record.amount,
                record.category,
                record.description,
                record.record_date,
                record.record_id,
            ),
        )

    return cursor.rowcount


def get_summary():
    _initialize_database()

    with _connect() as connection:
        income_total = connection.execute(
            """
            SELECT COALESCE(sum(amount), 0)
            FROM records
            WHERE record_type = ?
            """,
            ("income",),
        ).fetchone()[0]

        expense_total = connection.execute(
            """
            SELECT COALESCE(sum(amount), 0)
            FROM records
            WHERE record_type = ?
            """,
            ("expense",),
        ).fetchone()[0]

    balance = income_total - expense_total

    return {
        "income": income_total,
        "expense": expense_total,
        "balance": balance,
    }



def search_records_by_date(record_date):
    _initialize_database()
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT record_id, record_type, amount, category, description, record_date, created_at
            FROM records
            WHERE record_date = ?
            ORDER BY record_id DESC
            """,
            (record_date,),
        ).fetchall()

    return [Record.from_dict(dict(row)) for row in rows]
















