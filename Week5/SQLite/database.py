import sqlite3


def create_connection():
    conn = sqlite3.connect("users.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()  # noqa # .cursor creates a cursor object to execute SQL commands
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        SELECT users.*, courses.* 
            FROM users
            LEFT JOIN courses 
            ON courses.id = users.id
    ''')

    conn.commit()  # noqa # .commit saves the changes to the database
    conn.close()   # noqa # .close closes the connection to the database
