import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generates_password():
    passwd_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(passwd_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    
    print(f"Your password: {password}")

option = input("Do you want to generate a password? (Y/N) ").upper()

if option == "Y":
    generates_password()
elif option == "N":
    print("Program ended!")
    quit()
else:
    print("Invalid input! Please input 'Y' or 'N'")
    quit()