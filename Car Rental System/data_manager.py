from termcolor import colored
from database import create_connection
import sqlite3


def add_user(username, password, full_name, email, phone, role):
    # Validate role
    if role.lower() not in ['admin', 'staff']:
        print(colored("Error: Role must be either 'admin' or 'staff'", 'red', 'on_red'))
        return False

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, full_name, email, phone, role) VALUES (?, ?, ?, ?, ?, ?)",
            (username, password, full_name, email, phone, role.lower()))
        conn.commit()
        print(colored("User added successfully.", 'green', 'on_green'))
        return True
    except sqlite3.IntegrityError:
        print(colored("Username not already exist.", 'red', 'on_red'))
        return False
    conn.close()


def authenticate_login(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user[0] == password:  # Assuming password is stored in plain text
        return user[1]  # Return the role of the user (admin or staff)
    else:
        return None
    
def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def add_customer(full_name, email, phone, address, license_number):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO customers (full_name, email, phone, address, license_number) VALUES (?, ?, ?, ?, ?)", (full_name, email, phone, address, license_number))
        conn.commit()
        print("Customer added successfully.")
    except sqlite3.IntegrityError:
        print("License number or email already exists.")
    conn.close()


def add_cars(car_model, car_brand, year, color, daily_rate, status, registration_number):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO cars (car_model, car_brand, year, color, daily_rate, status, registration_number) VALUES (?, ?, ?, ?, ?)", (car_model, car_brand, year, color, daily_rate, status, registration_number))
        conn.commit()
        print("Car added successfully.")
    except sqlite3.IntegrityError:
        print("Registration number already exists.")
    conn.close()
