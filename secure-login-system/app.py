import hashlib
import os
import json

DB_FILE = "users.json"

def load_users():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def register():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    salt = os.urandom(16).hex()
    password_hash = hash_password(password, salt)

    users[username] = {
        "salt": salt,
        "hash": password_hash,
        "attempts": 0
    }

    save_users(users)
    print("User registered securely!")

def login():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    if username not in users:
        print("User not found")
        return

    user = users[username]

    if user["attempts"] >= 3:
        print("Account locked due to too many attempts.")
        return

    password_hash = hash_password(password, user["salt"])

    if password_hash == user["hash"]:
        print("Login successful!")
        user["attempts"] = 0
    else:
        user["attempts"] += 1
        print(f"Login failed. Attempts remaining: {3 - user['attempts']}")

    save_users(users)

while True:
    print("\n1 - Register")
    print("2 - Login")
    print("3 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        break
