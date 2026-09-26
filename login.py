users = {
    "admin": "admin123"
}


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False