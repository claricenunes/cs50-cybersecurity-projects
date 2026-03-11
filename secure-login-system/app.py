import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# convert password to hash
password_hash = hashlib.sha256(password.encode()).hexdigest()

print("\nUser created successfully!")
print("Username:", username)
print("Password hash:", password_hash)
