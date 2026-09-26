books = []


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author
    }

    books.append(book)

    print("Book added successfully.")


def display_books():
    if not books:
        print("No books available.")
        return

    print("\nAvailable Books")
    print("----------------")

    for book in books:
        print(
            "ID:", book["id"],
            "| Title:", book["title"],
            "| Author:", book["author"]
        )