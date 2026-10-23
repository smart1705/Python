def enter_text(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("Error: This field cannot be empty.")
        else:
            return text


def enter_age():
    while True:
        try:
            age = int(input("Enter age: "))

            if age > 0:
                return age
            else:
                print("Error: Age must be positive.")

        except ValueError:
            print("Error: Please enter a valid integer.")


def add_student(students):
    while True:
        roll_no = enter_text("Enter roll number: ")

        duplicate = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("Error: Roll number already exists.")
                duplicate = True
                break

        if not duplicate:
            break

    name = enter_text("Enter student name: ")
    course = enter_text("Enter course: ")
    age = enter_age()

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully.")


def search_student(students):
    roll_no = enter_text("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print_student(student)
            return

    print("Student not found.")


def update_student(students):
    roll_no = enter_text("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            name = enter_text("Enter new name: ")
            course = enter_text("Enter new course: ")
            age = enter_age()

            student["name"] = name
            student["course"] = course
            student["age"] = age

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    roll_no = enter_text("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def print_student(student):
    print("\nRoll Number:", student["roll_no"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])


def display_students(students):
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print_student(student)


def search_by_course(students):
    course = enter_text("Enter course to search: ")
    found = False

    for student in students:
        if student["course"].casefold() == course.casefold():
            print_student(student)
            found = True

    if not found:
        print("No students found in this course.")


def main():
    students = []

    while True:
        print("\n----- STUDENT DATA MANAGEMENT -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display Students")
        print("6. Search by Course")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            display_students(students)

        elif choice == "6":
            search_by_course(students)

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
