class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = "Available"


def find_book_by_id(books, book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None


def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return
    try:
        book_id = int(input("Enter book ID: "))
    except ValueError:
        print("Invalid book ID.")
        return

    if find_book_by_id(books, book_id) is not None:
        print("A book with this ID already exists.")
        return

    book = Book(title, author, book_id)
    books.append(book)
    print("Book added successfully!")


def view_books(books):
    if len(books) == 0:
        print("No books in the library.")
        return
    print("\nID    Title                Author               Status")
    print("-" * 60)
    for book in books:
        print(f"{book.book_id:<6}{book.title:<21}{book.author:<21}{book.status}")


def search_book(books):
    print("1. Search by ID")
    print("2. Search by Title")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            book_id = int(input("Enter book ID: "))
        except ValueError:
            print("Invalid book ID.")
            return
        book = find_book_by_id(books, book_id)
        if book is None:
            print("Book not found.")
        else:
            print(f"{book.book_id} - {book.title} by {book.author} - {book.status}")

    elif choice == "2":
        title = input("Enter title to search: ").strip().lower()
        found = False
        for book in books:
            if title in book.title.lower():
                print(f"{book.book_id} - {book.title} by {book.author} - {book.status}")
                found = True
        if not found:
            print("No book found with that title.")

    else:
        print("Invalid choice.")


def issue_book(books):
    try:
        book_id = int(input("Enter book ID to issue: "))
    except ValueError:
        print("Invalid book ID.")
        return

    book = find_book_by_id(books, book_id)
    if book is None:
        print("Book not found.")
    elif book.status == "Issued":
        print("This book is already issued.")
    else:
        book.status = "Issued"
        print("Book issued successfully.")


def return_book(books):
    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Invalid book ID.")
        return

    book = find_book_by_id(books, book_id)
    if book is None:
        print("Book not found.")
    elif book.status == "Available":
        print("This book is already available. It was not issued.")
    else:
        book.status = "Available"
        print("Book returned successfully.")


def delete_book(books):
    try:
        book_id = int(input("Enter book ID to delete: "))
    except ValueError:
        print("Invalid book ID.")
        return

    book = find_book_by_id(books, book_id)
    if book is None:
        print("Book not found.")
    else:
        books.remove(book)
        print("Book deleted successfully.")


def main():
    books = []
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()