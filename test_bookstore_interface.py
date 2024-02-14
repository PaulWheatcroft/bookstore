import unittest
from unittest.mock import MagicMock
from bookstore_interface import create_book


class TestCreateBook(unittest.TestCase):
    def test_insert_new_book_valid_data(self):
        conn = MagicMock()
        book = {
            'ISBN': '1234567890',
            'title': 'Test Book',
            'author': 'Test Author',
            'year': 2022,
            'stock': 100,
            'price': 20.00,
        }
        result = create_book(conn, book)
        self.assertIsNotNone(result)

    def test_insert_new_book_missing_data(self):
        conn = MagicMock()
        book = {
            'ISBN': '1234567890',
            'title': 'Test Book',
            'author': 'Test Author',
            'year': 2022,
            'stock': 100,
        }
        result = create_book(conn, book)
        self.assertIsNone(result)

    def test_handle_database_error(self):
        conn = MagicMock()
        conn.commit.side_effect = Exception("Database error")
        book = {
            'ISBN': '1234567890',
            'title': 'Test Book',
            'author': 'Test Author',
            'year': 2022,
            'stock': 100,
            'price': 20.00,
        }
        result = create_book(conn, book)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
