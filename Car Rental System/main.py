from termcolor import colored
from database import create_table
from data_manager import add_user, authenticate_login, view_users
import os
import msvcrt  # For Windows key press detection


def press_any_key():
    print(colored("\nPress any key to continue...", 'yellow', 'on_blue'))
    msvcrt.getch()  # Wait for any key press
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Welcome to the Car Rental System", 'green', 'on_yellow'))
    print("1. Staff Login")
    print("2. Customer Login")
    print("3. Exit")


def main_menu():
    create_table()
    while True:
        main()
        choice = input("Enter your choice: ")
        if choice == "1":
            staff_login()
        elif choice == "2":
            print("Customer Login")
        elif choice == "3":
            print(colored("Exiting the program...", 'green', 'on_red'))
            break
        else:
            print(colored("Invalid choice! Select from 1-3", 'green', 'on_red'))
            press_any_key()


def staff_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Staff Login", 'green', 'on_blue'))
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = authenticate_login(username, password)
    if role:
        if role in ['admin', 'staff']:
            print(colored("Login successful!", 'green', 'on_green'))
            if role == 'admin':
                print(colored("Welcome, Admin!", 'green', 'on_green'))
                press_any_key()
                admin_choice()
            elif role == 'staff':
                print("Welcome, Staff!")
                press_any_key()
        else:
            print(colored(
                "Access denied! Only admin and staff roles are allowed.", 'green', 'on_red'))
            press_any_key()
    else:
        print(colored("Invalid username or password!", 'green', 'on_red'))
        press_any_key()


def admin_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Admin Menu", 'green', 'on_blue'))
    print("1. Register Staff")
    print("2. View Staff")
    print("3. View Cars")
    print("4. Add Car")
    print("5. Update Car")
    print("6. Delete Car")
    print("7. View Customers")
    print("8. Add Customer")
    print("9. Update Customer")
    print("10. Delete Customer")
    print("0. Exit")


def admin_choice():
    while True:
        admin_menu()
        choice = input("Enter your choice 0-9: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '1':
            print(colored("Register Staff", 'green', 'on_blue'))
            username = input("Enter username: ")
            password = input("Enter password: ")
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            role = input("Enter role (admin/staff): ")
            if add_user(username, password, full_name, email, phone, role):
                print(colored("Staff registration completed!", 'green', 'on_green'))
            press_any_key()

        elif choice == '2':
            print(colored("View Staff", 'green', 'on_blue'))
            users = view_users()
            for user in users:
                print(user)
            press_any_key()

        else:
            print(colored("Invalid choice! Select from 0-9", 'green', 'on_red'))
            press_any_key()


if __name__ == "__main__":
    main_menu()
