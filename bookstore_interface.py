from sqlite3 import Error
import sqlite3
from colorama import Fore, Style

conn = sqlite3.connect("bookstore.db")

print("****", conn)


def create_book(conn, book):
    # Implement the logic to insert a new book into the database
    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO books (ISBN, title, author, year, stock, price)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (
                book['ISBN'],
                book['title'],
                book['author'],
                book['year'],
                book['stock'],
                book['price'],
            ),
        )
        conn.commit()
        return cursor
    except Error as e:
        print(e)
        return None


def read_books(conn):
    # Implement the logic to retrieve books from the database
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        for book in books:
            print(Fore.GREEN + str(book))
        return books
    except Error as e:
        print(e)
        return None


def update_book(conn, book):
    # Implement the logic to update a book in the database
    pass


def delete_book(conn, id):
    # Implement the logic to delete a book from the database
    pass


def main():
    print("Welcome to the Bookstore Interface")
    while True:
        print(Fore.BLUE + "Select an option:")
        print(Fore.YELLOW + "1. Create a book")
        print(Fore.YELLOW + "2. Read books")
        print(Fore.YELLOW + "3. Update a book")
        print(Fore.YELLOW + "4. Delete a book")
        print(Fore.RED + "5. Exit")
        choice = input(Fore.BLUE + "Enter your choice: ")

        if choice == "1":
            # Logic to create a book
            book = {
                'ISBN': input("Enter the ISBN of the book: "),
                'title': input("Enter the title of the book: "),
                'author': input("Enter the author of the book: "),
                'year': input("Enter the year of publication: "),
                'stock': input("Enter the number of copies: "),
                'price': input("Enter the price of the book: "),
            }

            cursor = create_book(conn, book)

            if cursor:
                print("Book created successfully")
                for row in cursor:
                    print(row)
            else:
                print("Failed to create book")

            # ... (prompt for other book details and call create_book function)
        elif choice == "2":
            # Logic to read books
            read_books(conn)
        elif choice == "3":
            # Logic to update a book
            print("Exiting the Bookstore Interface")
            break
        elif choice == "4":
            # Logic to delete a book
            print("Exiting the Bookstore Interface")
            break
        elif choice == "5":
            print("Exiting the Bookstore Interface")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
