# Smart Login System 

import getpass

correct_username = "admin"
correct_password = "pass@123"
active = True
max_attempts = 3

attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ")

    if not active:
        print("Account Disabled")
        break

    if username == correct_username.lower() and password == correct_password:
        print("Login Successful ")
        break
    else:
        attempts += 1
        print(f"Wrong Credentials  | Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Account Locked due to multiple failed attempts ")
