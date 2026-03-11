# Secure Login System 

A secure authentication system demonstrating cybersecurity concepts such as 
password hashing, salting, and brute-force protection.

Developed while studying Harvard's CS50 Cybersecurity.

---

## Demo

User registration and login system with secure password storage.

Example login attempt:

Login failed  
Attempts remaining: 2

---

## Authentication Flow

```mermaid
flowchart TD
A[User enters password] --> B[Add Salt]
B --> C[Hash Password]
C --> D[Compare with Stored Hash]
D --> E{Match?}
E -->|Yes| F[Login Success]
E -->|No| G[Login Failed]
```

## Security Concepts Implemented

- Password Hashing
- Salting
- Rate Limiting
- Brute-force Protection
- Secure Authentication Flow

---

## Attack Scenario

Brute-force attacks attempt to guess passwords by trying many combinations.

Example passwords used in attacks:

123456  
password  
qwerty  
admin123  

---

## Defense Mechanisms

This system implements:

- Password hashing using SHA-256
- Unique salt for each password
- Login attempt limits
- Temporary account lockout

---

## Project Structure

```
secure-login-system
 ├── app.py
 ├── users.json
 └── README.md
```

---

## How to Run

Clone the repository:

```
git clone https://github.com/claricenunes/cs50-cybersecurity-projects
```

Run the application:

```
python app.py
```

---

## What I Learned

Through this project I learned:

- how password hashing works
- why salting is important
- how brute-force attacks operate
- how authentication systems defend against attacks
