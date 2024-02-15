from sqlite3 import Error
import sqlite3
from colorama import Fore, Style

conn = sqlite3.connect("bookstore.db")


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
    try:
        print('update_book', book)
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE books
            SET title = ?, author = ?, year = ?, stock = ?, price = ?
            WHERE ISBN = ?""",
            (
                book['title'],
                book['author'],
                book['year'],
                book['stock'],
                book['price'],
                book['ISBN'],
            ),
        )
        conn.commit()
        return cursor
    except Error as e:
        print(e)
        return None


def delete_book(conn, id):
    # Implement the logic to delete a book from the database
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE ISBN = ?", (id,))
        conn.commit()
        return cursor
    except Error as e:
        print(e)
        return None


def main():
    print(Fore.MAGENTA + Style.BRIGHT + "**********************************")
    print(Fore.MAGENTA + "Welcome to the Bookstore Interface")
    print(
        Fore.MAGENTA
        + Style.BRIGHT
        + "**********************************"
        + Style.RESET_ALL
    )
    while True:
        print(Fore.LIGHTWHITE_EX + "Select an option:")
        print(Fore.LIGHTYELLOW_EX + "==================================")
        print(Fore.YELLOW + "1. Create a book")
        print(Fore.YELLOW + "2. Read books")
        print(Fore.YELLOW + "3. Update a book")
        print(Fore.YELLOW + "4. Delete a book")
        print(Fore.RED + "5. Exit")
        print(Fore.LIGHTYELLOW_EX + "==================================")
        choice = input(Fore.LIGHTWHITE_EX + "Enter your choice: ")

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
                print(
                    Fore.GREEN
                    + Style.BRIGHT
                    + "Book created successfully"
                    + Style.RESET_ALL
                )
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
            # get a book title based on ISBN
            def get_book(isbn):
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books WHERE ISBN = ?", (isbn,))
                book = cursor.fetchone()
                print('get_book', book)
                if book:
                    book_dict = {
                        'ISBN': book[5],
                        'title': book[0],
                        'author': book[1],
                        'year': book[2],
                        'stock': book[3],
                        'price': book[4],
                    }
                    return book_dict
                else:
                    return None

            book = get_book(input("Enter the ISBN of the book: "))

            print(Fore.GREEN + str(book))

            if not book:
                print("Book not found")
                return

            updated_book = {
                'ISBN': book['ISBN'],
                'title': input("Enter the title of the book: "),
                'author': input("Enter the author of the book: "),
                'year': input("Enter the year of publication: "),
                'stock': input("Enter the number of copies: "),
                'price': input("Enter the price of the book: "),
            }

            update_book(conn, updated_book)
            print("Book updated successfully")
        elif choice == "4":
            # Logic to delete a book
            isbn = input("Enter the ISBN of the book: ")
            confirmation = input(
                "Are you sure you want to delete the book? (yes/no): "
            )
            if confirmation.lower() == "yes":
                delete_book(conn, isbn)
                print("Book deleted successfully")
            else:
                print("Delete canceled")
        elif choice == "5":
            print("Exiting the Bookstore Interface")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
