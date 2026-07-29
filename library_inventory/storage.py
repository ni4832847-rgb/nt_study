import json
from pathlib import Path

from book import Book


DATA_FILE = Path(__file__).with_name("books.json")


def load_books():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [Book.from_dict(item) for item in data]


def save_books(books):
    data = [book.to_dict() for book in books]

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
