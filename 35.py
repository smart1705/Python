CollegeManagement/
storage.py
student.py
result.py
attendance.py
report.py
main.py


File 1: storage.py
import json
import os


def load_data(file_name, default_data):
    if not os.path.exists(file_name):
        if save_data(file_name, default_data):
            return default_data.copy()

        return None

    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        if not isinstance(data, type(default_data)):
            print("Error: Invalid data format in", file_name)
            return None

        return data

    except (json.JSONDecodeError, OSError):
        print("Error reading file:", file_name)
        return None


def save_data(file_name, data):
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        print("Error saving file:", file_name)
        return False


def enter_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text
        else:
            print("Error: This field cannot be empty.")


def enter_marks(message):
    while True:
        try:
            marks = float(input(message))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Error: Marks must be between 0 and 100.")

        except ValueError:
            print("Error: Enter valid numeric marks.")


def enter_whole_number(message, minimum=0):
    while True:
        try:
            number = int(input(message))

            if number >= minimum:
                return number
            else:
                print("Error: Enter a number greater than or equal to", minimum)

        except ValueError:
            print("Error: Enter a valid whole number.")


File 2: student.py
from storage import load_data, save_data, enter_text

FILE_NAME = "students35.json"

def add_student():
    students = load_data(FILE_NAME, [])

    if students is None:
        return

    while True:
        roll_no = enter_text("Enter roll number: ")

        if any(student["roll_no"] == roll_no for student in students):
            print("Error: Roll number already exists.")
        else:
            break

    name = enter_text("Enter student name: ")
    course = enter_text("Enter course: ")

    record = {
        "roll_no": roll_no,
        "name": name,
        "course": course
    }

    students.append(record)

    if save_data(FILE_NAME, students):
        print("Student added successfully.")


def search_student(roll_no):
    students = load_data(FILE_NAME, [])

    if students is None:
        return None

    for student in students:
        if student["roll_no"] == roll_no:
            return student

    return None


def display_students():
    students = load_data(FILE_NAME, [])

    if students is None:
        return

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nRoll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Course:", student["course"])


File 3: result.py
from storage import load_data, save_data, enter_text, enter_marks
from student import search_student

FILE_NAME = "results35.json"


def enter_result():
    while True:
        roll_no = enter_text("Enter roll number: ")
        student = search_student(roll_no)

        if student is not None:
            break

        print("Student not found. Add the student first or try again.")

    marks = enter_marks("Enter marks (0-100): ")

    results = load_data(FILE_NAME, {})

    if results is None:
        return

    results[roll_no] = marks

    if save_data(FILE_NAME, results):
        print("Result saved successfully.")


def get_result(roll_no):
    results = load_data(FILE_NAME, {})

    if results is None or roll_no not in results:
        return None

    marks = results[roll_no]

    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return marks, status


File 4: attendance.py
from storage import load_data, save_data, enter_text, enter_whole_number
from student import search_student

FILE_NAME = "attendance35.json"


def record_attendance():
    while True:
        roll_no = enter_text("Enter roll number: ")
        student = search_student(roll_no)

        if student is not None:
            break

        print("Student not found. Add the student first or try again.")

    while True:
        attended = enter_whole_number("Enter classes attended: ")
        total = enter_whole_number("Enter total classes: ")

        if attended > total:
            print("Error: Attended classes cannot exceed total classes.")
        else:
            break

    records = load_data(FILE_NAME, {})

    if records is None:
        return

    records[roll_no] = {
        "attended": attended,
        "total": total
    }

    if save_data(FILE_NAME, records):
        print("Attendance saved successfully.")


def get_attendance(roll_no):
    records = load_data(FILE_NAME, {})

    if records is None or roll_no not in records:
        return None

    attended = records[roll_no]["attended"]
    total = records[roll_no]["total"]

    if total == 0:
        percentage = 0
    else:
        percentage = attended / total * 100

    if percentage < 75:
        status = "Low Attendance"
    else:
        status = "Satisfactory"

    return percentage, status


File 5: report.py
from storage import enter_text
from student import search_student
from result import get_result
from attendance import get_attendance


def generate_report():
    while True:
        roll_no = enter_text("Enter roll number: ")
        student = search_student(roll_no)

        if student is not None:
            break

        print("Student not found. Try again.")

    print("\n===== STUDENT REPORT =====")
    print("Roll Number:", student["roll_no"])
    print("Name:", student["name"])
    print("Course:", student["course"])

    result = get_result(roll_no)

    if result is None:
        print("Result: Not entered")
    else:
        marks, status = result
        print("Marks:", marks)
        print("Result Status:", status)

    attendance = get_attendance(roll_no)

    if attendance is None:
        print("Attendance: Not recorded")
    else:
        percentage, status = attendance
        print("Attendance:", round(percentage, 2), "%")
        print("Attendance Status:", status)

    print("==========================")

File 6: main.py
from storage import enter_text
from student import add_student, search_student, display_students
from result import enter_result
from attendance import record_attendance
from report import generate_report


def main():
    while True:
        print("\n===== COLLEGE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display Students")
        print("4. Enter Student Result")
        print("5. Record Attendance")
        print("6. Generate Student Report")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            roll_no = enter_text("Enter roll number: ")
            student = search_student(roll_no)

            if student is None:
                print("Student not found.")
            else:
                print("\nRoll Number:", student["roll_no"])
                print("Name:", student["name"])
                print("Course:", student["course"])

        elif choice == "3":
            display_students()

        elif choice == "4":
            enter_result()

        elif choice == "5":
            record_attendance()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            print("College Management System closed.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()s
