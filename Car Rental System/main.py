from termcolor import colored
from database import create_table
from data_manager import add_user, authenticate_login, view_users, view_customers, view_cars, add_customer, add_cars, search_customer, search_car, del_car
import os
import msvcrt  # For Windows key press detection


class CarRental:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarRental, cls).__new__(cls)
        return cls._instance


class User(CarRental):
    def __init__(self):
        self.username = None
        self.password = None
        self.full_name = None
        self.email = None
        self.phone = None
        self.role = None

    def set_user(self, username, password, full_name, email, phone, role):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.role = role

    def get_user(self):
        return {
            'username': self.username,
            'password': self.password,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'role': self.role
        }


class Customer(CarRental):
    def __init__(self):
        self.full_name = None
        self.email = None
        self.phone = None
        self.address = None
        self.license_number = None

    def set_customer(self, full_name, email, phone, address, license_number):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.license_number = license_number

    def get_customer(self):
        return {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'license_number': self.license_number
        }


class Car(CarRental):
    def __init__(self):
        self.car_model = None
        self.car_brand = None
        self.year = None
        self.color = None
        self.daily_rate = None
        self.status = None
        self.registration_number = None

    def set_car(self, car_model, car_brand, year, color, daily_rate, status, registration_number):
        self.car_model = car_model
        self.car_brand = car_brand
        self.year = year
        self.color = color
        self.daily_rate = daily_rate
        self.status = status
        self.registration_number = registration_number

    def get_car(self):
        return {
            'car_model': self.car_model,
            'car_brand': self.car_brand,
            'year': self.year,
            'color': self.color,
            'daily_rate': self.daily_rate,
            'status': self.status,
            'registration_number': self.registration_number
        }


def press_any_key():
    print(colored("\nPress any key to continue...", 'yellow', 'on_blue'))
    msvcrt.getch()  # Wait for any key press
    os.system('cls')


def press_any_key2():
    print(colored("\nPress any key to continue...", 'yellow', 'on_blue'))
    msvcrt.getch()  # Wait for any key press


def main():
    os.system('cls')
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
    os.system('cls')
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
    os.system('cls')
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
            user = User()
            user.set_user(
                input("Enter username: "),
                input("Enter password: "),
                input("Enter full name: "),
                input("Enter email: "),
                input("Enter phone number: "),
                input("Enter role (admin/staff): ")
            )
            if add_user(**user.get_user()):
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

        else:
            print(colored("Invalid choice! Select from 0-4", 'green', 'on_red'))
            press_any_key()


def customer_menu():
    os.system('cls')
    print(colored("Customer Menu", 'green', 'on_blue'))
    print("1. View Customers")
    print("2. Add Customer")
    print("3. Search Customer")
    print("4. Back")
    print("0. Exit")


def customer_menu_choice():
    while True:
        customer_menu()
        choice = input("Enter your choice 0-4: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '4':
            admin_menu_choice()
        elif choice == '1':
            print(colored("View Staff", 'green', 'on_blue'))
            customers = view_customers()
            for customer in customers:
                print(customer)
            press_any_key()

        elif choice == '2':
            print(colored("Register New Customer", 'green', 'on_blue'))
            customer = Customer()
            customer.set_customer(
                input("Enter full name: ").lower(),
                input("Enter email: "),
                input("Enter phone number: "),
                input("Enter address: "),
                input("Enter license number: ").lower()
            )
            if add_customer(**customer.get_customer()):
                print(colored("Customer registration completed!", 'green', 'on_green'))
            press_any_key()

        elif choice == '3':
            print(colored("Search Customer ", 'green', 'on_blue'))
            name = input("Enter name: ").lower()
            license_number = input("Enter license number: ").lower()
            customer = search_customer(name, license_number)
            if customer:
                print(customer)
            else:
                print(colored("Customer not found!", 'green', 'on_red'))
            press_any_key()

        else:
            print(colored("Invalid choice! Select from 0-4", 'green', 'on_red'))
            press_any_key()


def car_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Car Menu", 'green', 'on_blue'))
    print("1. View Cars")
    print("2. Add Car")
    print("3. Search Car")
    print("4. Back")
    print("0. Exit")


def car_menu_choice():
    while True:
        car_menu()
        choice = input("Enter your choice 0-4: ")
        if choice == '0':
            print(colored("Exiting the program...", 'green', 'on_red'))
            exit()
        elif choice == '4':
            admin_menu_choice()
        elif choice == '1':
            print(colored("View Staff", 'green', 'on_blue'))
            cars = view_cars()
            for car in cars:
                print(car)
            press_any_key()

        elif choice == '2':
            print(colored("Register New Car", 'green', 'on_blue'))
            car_model = input("Enter car model: ").lower()
            car_brand = input("Enter car brand: ")
            year = input("Enter year: ")
            color = input("Enter color: ")
            daily_rate = input("Enter daily rate: ")
            status = 'available'
            registration_number = input("Enter registration number: ").lower()
            if add_cars(car_model.lower(), car_brand, year, color, daily_rate, status, registration_number):
                print(colored("Car registration completed!", 'green', 'on_green'))
            press_any_key()

        elif choice == '3':
            print(colored("Search Car ", 'green', 'on_blue'))
            car_model = input("Enter car model: ").lower()
            registration_number = input("Enter registration number: ").lower()
            car = search_car(car_model, registration_number)
            if car:
                while True:
                    print(car)
                    print(colored("Select an option", 'green', 'on_blue'))
                    print("1. Delete Car")
                    print("2. Edit Car")
                    print("3. Back Car")
                    choice = input("Select an option: ")
                    if choice == '1':
                        del_car(registration_number)
                        print("Car successfully deleted!")
                        press_any_key2()
                        car_menu_choice()
                    elif choice == '3':
                        car_menu_choice()
                    else:
                        print(
                            colored("Invalid choice! Select from 1-3", 'green', 'on_red'))
                        press_any_key2()

            else:
                print(colored("Car not found!", 'green', 'on_red'))
                press_any_key()

        else:
            print(colored("Invalid choice! Select from 0-4", 'green', 'on_red'))
            press_any_key()


if __name__ == "__main__":
    main_menu()
