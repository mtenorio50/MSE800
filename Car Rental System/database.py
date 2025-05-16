import sqlite3


def create_connection():
    conn = sqlite3.connect("car_rental.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()  # noqa # .cursor creates a cursor object to execute SQL commands

    # Create Users table (for system users/employees)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'staff')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            license_number TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create Cars table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_model TEXT NOT NULL,
            car_brand TEXT NOT NULL,
            year INTEGER NOT NULL,
            color TEXT NOT NULL,
            daily_rate DECIMAL(10,2) NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('available', 'rented', 'maintenance')),
            registration_number TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create Rentals table to track rental transactions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            rental_date TIMESTAMP NOT NULL,
            return_date TIMESTAMP,
            total_amount DECIMAL(10,2),
            status TEXT NOT NULL CHECK(status IN ('active', 'completed', 'cancelled')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (car_id) REFERENCES cars (id),
            FOREIGN KEY (customer_id) REFERENCES customers (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()  # noqa # .commit saves the changes to the database
    conn.close()   # noqa # .close closes the connection to the database


if __name__ == "__main__":
    create_table()
