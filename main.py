import json
import os
from encrypt import encrypt, decrypt

DB_FILE = "database.json"

# Create file if not present
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as db:
        json.dump({}, db)

def load_db():
    with open(DB_FILE, "r") as db:
        return json.load(db)

def save_db(data):
    with open(DB_FILE, "w") as db:
        json.dump(data, db, indent=4)

def add_password():
    site = input("Enter website/app name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    encrypted_password = encrypt(password).decode()

    data = load_db()
    data[site] = {"username": username, "password": encrypted_password}

    save_db(data)
    print("Password saved!")

def view_passwords():
    data = load_db()
    if not data:
        print("No passwords saved yet.")
        return

    for site, info in data.items():
        decrypted_password = decrypt(info["password"].encode())
        print(f"\nSite: {site}")
        print(f"Username: {info['username']}")
        print(f"Password: {decrypted_password}")

def delete_password():
    site = input("Enter website name to delete: ")
    data = load_db()

    if site in data:
        del data[site]
        save_db(data)
        print("Entry deleted.")
    else:
        print("No such site found.")

def main():
    print("Simple Password Manager")
    print("---------------------------")

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
