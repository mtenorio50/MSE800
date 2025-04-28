# Add student and record their grades, then display the records
class grading:  # student grading class

    # Constructor to initialize the student's attributes
    def __init__(self, name, grade1, grade2):
        self.name = name  # student name
        self.grade1 = grade1  # grade1 of the student
        self.grade2 = grade2  # grade2 of the student

    def add_student(record):  # function to add a student to the record
        name = input("Enter student name: ")
        grade1 = int(input("Enter grade1: "))
        grade2 = int(input("Enter grade2: "))

        # create a new student object with the provided name and grades
        student = grading(name, grade1, grade2)
        record.append(student)  # add the student to the record list

    def show_students(record): # function to show all students in the record
        print("Student Records:")
        for grading in record: # iterate through the record list
            print(
                f"Name: {grading.name}, Grade1: {grading.grade1}, Grade2: {grading.grade2}")
            print("-----------------------")


record = []

grading.add_student(record)
grading.add_student(record)

grading.show_students(record)
