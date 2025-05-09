from database import create_connection
import sqlite3


def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()


def add_course(course_name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO courses (course_name, unit) VALUES (?, ?)", (course_name, unit))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Error on input.")
    conn.close()


def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()  # noqa # .fetchall retrieves all rows from the result set
    conn.close()  # noqa # .close closes the connection to the database
    return rows


def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()  # noqa # .fetchall retrieves all rows from the result set
    conn.close()  # noqa # .close closes the connection to the database
    return rows


def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))  # noqa # .execute executes a SQL command / WHERE name LIKE ? is a SQL command to search for a name
    rows = cursor.fetchall()  # noqa # .fetchall retrieves all rows from the result set
    conn.close()
    return rows


def advance_search(id, name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND name = ?", (id, name))
    rows = cursor.fetchall()
    conn.close()
    return rows


def adv_search_course_and_name(name, course_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    users = cursor.fetchall()
    cursor.execute(
        "SELECT * FROM courses WHERE course_name = ?", (course_name,))
    courses = cursor.fetchall()
    conn.close()
    if users and courses:
        return users, courses
    else:
        return []


def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("��️ User deleted.")
