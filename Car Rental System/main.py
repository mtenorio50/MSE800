from termcolor import colored
from database import create_table
from data_manager import add_user, authenticate_login


def main():
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


def staff_login():
    print("Staff Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = authenticate_login(username, password)
    if role:
        if role in ['admin', 'staff']:
            print(colored("Login successful!", 'green', 'on_green'))
            if role == 'admin':
                print("Welcome, Admin!")
                admin_choice()
            elif role == 'staff':
                print("Welcome, Staff!")
        else:
            print(colored(
                "Access denied! Only admin and staff roles are allowed.", 'green', 'on_red'))
    else:
        print(colored("Invalid username or password!", 'green', 'on_red'))


def admin_menu():
    print(colored("Admin Menu", 'green', 'on_blue'))
    print("1. Register Staff")
    print("2. View Cars")
    print("3. Add Car")
    print("4. Update Car")
    print("5. Delete Car")
    print("6. View Customers")
    print("7. Add Customer")
    print("8. Update Customer")
    print("9. Delete Customer")
    print("0. Exit")


def admin_choice():
    while True:
        admin_menu()
        choice = input("Enter your choice 0-9: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '1':
            print("Register Staff")
            username = input("Enter username: ")
            password = input("Enter password: ")
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            role = input("Enter role (admin/staff): ")
            add_user(username, password, full_name, email, phone, role)
        else:
            print(colored("Invalid choice! Select from 0-9", 'green', 'on_red'))


if __name__ == "__main__":
    main_menu()
