from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advance_search, view_courses, add_course, adv_search_course_and_name


def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Search User by ID and Name")
    print("7. Add Course")
    print("8. View All Courses")
    print("9. Search User by Course and Name")
 

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)

        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == '6':
            studid = input("Enter Student ID to search: ")
            name = input("Enter name to search: ")
            users = advance_search(studid, name)
            if users:
                for user in users:
                    print(user)
            else:
                print("No Records found!")

        elif choice == '7':
            coursename = input("Enter course name: ")
            unit = input("Enter course unit: ")
            add_course(coursename, unit)

        elif choice == '8':
            courses = view_courses()
            for course in courses:
                print(course)

        elif choice == '9':
            name = input("Enter name to search: ")
            coursename = input("Enter course name to search: ")
            result = adv_search_course_and_name(name, coursename)
            if result:
                users, courses = result
                print("Users found:")
                for user in users:
                    print(user)
                print("Courses found:")
                for course in courses:
                    print(course)
            else:
                print("No Records found!")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
