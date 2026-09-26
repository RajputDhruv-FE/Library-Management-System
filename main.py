from login import login
from books import add_book, display_books

print("Library Management System")
print("-------------------------")

if login():

    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")