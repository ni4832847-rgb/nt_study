import unittest
from unittest.mock import patch

import manager


class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.book = manager.Book(
            book_id="1",
            title="Python入门",
            author="张三",
            category="编程",
            total_stock=5,
            available_stock=3,
        )
        self.books = [self.book]

    def test_borrow_book_decreases_available_stock(self):
        with patch.object(manager, "load_books", return_value=self.books), \
                patch.object(manager, "save_books"), \
                patch("builtins.input", side_effect=["1", "张三"]), \
                patch.object(manager, "load_records", return_value=[]), \
                patch.object(manager, "save_records"):
            manager.borrow_book()

        self.assertEqual(self.book.available_stock, 2)

    def test_return_book_increases_available_stock(self):
        with patch.object(manager, "load_books", return_value=self.books), \
                patch.object(manager, "save_books"), \
                patch("builtins.input", side_effect=["1", "张三"]), \
                patch.object(
                    manager,
                    "load_records",
                    return_value=[
                        {"book_id": "1", "borrower": "张三", "returned": False}
                    ],
                ), \
                patch.object(manager, "save_records"):
            manager.return_book()

        self.assertEqual(self.book.available_stock, 4)

    def test_update_stock_keeps_borrowed_count(self):
        with patch.object(manager, "load_books", return_value=self.books), \
                patch.object(manager, "save_books"), \
                patch("builtins.input", side_effect=["1", "6"]):
            manager.update_stock()

        self.assertEqual(self.book.total_stock, 6)
        self.assertEqual(self.book.available_stock, 4)

    def test_update_stock_rejects_negative_value(self):
        with patch.object(manager, "load_books", return_value=self.books), \
                patch.object(manager, "save_books"), \
                patch("builtins.input", side_effect=["1", "-1"]):
            manager.update_stock()

        self.assertEqual(self.book.total_stock, 5)
        self.assertEqual(self.book.available_stock, 3)

    def test_search_book_matches_author(self):
        with patch.object(manager, "load_books", return_value=self.books), \
                patch("builtins.input", return_value="张三"), \
                patch("builtins.print") as mocked_print:
            manager.search_book()

        self.assertTrue(mocked_print.called)
        output = "\n".join(str(call) for call in mocked_print.call_args_list)
        self.assertIn("Python入门", output)

    def test_list_borrow_records_displays_status(self):
        records = [
            {
                "book_id": "1",
                "book_title": "Python入门",
                "borrower": "张三",
                "borrowed_at": "2026-07-21 10:00:00",
                "returned_at": None,
                "returned": False,
            }
        ]
        with patch.object(manager, "load_records", return_value=records), \
                patch("builtins.print") as mocked_print:
            manager.list_borrow_records()

        output = "\n".join(str(call) for call in mocked_print.call_args_list)
        self.assertIn("借阅中", output)


if __name__ == "__main__":
    unittest.main()
