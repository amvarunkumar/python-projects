import random

def generate_password(length):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_chars = "!@#$%^&*()"
    all_chars = letters + numbers + special_chars

    password = ""
    for i in range(length):
        password += random.choice(all_chars)

    return password

while True:
    try:
        password_length = int(input("Enter the desired password length: "))

        generate_password = generate_password(password_length)
        print(f"Generated Password : {generate_password}")

        another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if another != "yes":
            print("Bye Bye!")
            break

    except ValueError:
        print("Please enter a valid number for the password length.")
