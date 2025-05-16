from termcolor import colored
from database import create_table
from data_manager import add_user, authenticate_login, view_users, view_customers, view_cars, add_customer, add_cars
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
                admin_menu_choice()
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
    print("3. Car Management")
    print("4. Customer Management")
    print("0. Exit")


def admin_menu_choice():
    while True:
        admin_menu()
        choice = input("Enter your choice 0-4: ")
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

        elif choice == '3':
            car_menu_choice()

        elif choice == '4':
            customer_menu_choice()

        elif choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()

        else:
            print(colored("Invalid choice! Select from 0-4", 'green', 'on_red'))
            press_any_key()


def customer_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Customer Menu", 'green', 'on_blue'))
    print("1. View Customers")
    print("2. Add Customer")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. Back")
    print("0. Exit")


def customer_menu_choice():
    while True:
        customer_menu()
        choice = input("Enter your choice 0-4: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '5':
            admin_menu_choice()
        elif choice == '1':
            print(colored("View Staff", 'green', 'on_blue'))
            customers = view_customers()
            for customer in customers:
                print(customer)
            press_any_key()

        elif choice == '2':
            print(colored("Register New Customer", 'green', 'on_blue'))
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            license_number = input("Enter license number: ")
            if add_customer(full_name, email, phone, address, license_number):
                print(colored("Customer registration completed!", 'green', 'on_green'))
            press_any_key()

        else:
            print(colored("Invalid choice! Select from 0-5", 'green', 'on_red'))
            press_any_key()


def car_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Car Menu", 'green', 'on_blue'))
    print("1. View Cars")
    print("2. Add Car")
    print("3. Update Car")
    print("4. Delete Car")
    print("5. Back")
    print("0. Exit")


def car_menu_choice():
    while True:
        car_menu()
        choice = input("Enter your choice 0-4: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '5':
            admin_menu_choice()
        elif choice == '1':
            print(colored("View Staff", 'green', 'on_blue'))
            cars = view_cars()
            for car in cars:
                print(car)
            press_any_key()

        elif choice == '2':
            print(colored("Register New Car", 'green', 'on_blue'))
            car_model = input("Enter car model: ")
            car_brand = input("Enter car brand: ")
            year = input("Enter year: ")
            color = input("Enter color: ")
            daily_rate = input("Enter daily rate: ")
            status = 'available'
            registration_number = input("Enter registration number: ")
            if add_cars(car_model, car_brand, year, color, daily_rate, status, registration_number):
                print(colored("Car registration completed!", 'green', 'on_green'))
            press_any_key()

        else:
            print(colored("Invalid choice! Select from 0-5", 'green', 'on_red'))
            press_any_key()


if __name__ == "__main__":
    main_menu()
