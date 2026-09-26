from login import login
from books import add_book, display_books
from students import register_student, display_students

print("Library Management System")
print("-------------------------")

if login():

    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Register Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            register_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")