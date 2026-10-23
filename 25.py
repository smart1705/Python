class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.results = {}

    def display(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Enrolled Courses:", self.courses)


class Faculty:
    def __init__(self, faculty_id, name, age, subject, salary):
        self.faculty_id = faculty_id
        self.name = name
        self.age = age
        self.subject = subject
        self.salary = salary

    def display(self):
        print("\nFaculty ID:", self.faculty_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("Salary:", self.salary)


class Course:
    def __init__(self, course_id, course_name, faculty_id):
        self.course_id = course_id
        self.course_name = course_name
        self.faculty_id = faculty_id

    def display(self):
        print("\nCourse ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Faculty ID:", self.faculty_id or "Not Assigned")


class College:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}

    def enter_text(self, message):
        while True:
            text = input(message).strip()

            if text:
                return text
            else:
                print("Error: This field cannot be empty.")

    def enter_unique_id(self, records, message):
        while True:
            record_id = self.enter_text(message)

            if record_id not in records:
                return record_id
            else:
                print("Error: ID already exists. Enter another ID.")

    def enter_age(self):
        while True:
            try:
                age = int(input("Enter age: "))

                if age > 0:
                    return age
                else:
                    print("Error: Age must be greater than 0.")

            except ValueError:
                print("Error: Enter a valid whole number.")

    def enter_salary(self):
        while True:
            try:
                salary = float(input("Enter salary: "))

                if salary >= 0:
                    return salary
                else:
                    print("Error: Salary cannot be negative.")

            except ValueError:
                print("Error: Enter a valid numeric salary.")

    def enter_marks(self):
        while True:
            try:
                marks = float(input("Enter marks (0-100): "))

                if 0 <= marks <= 100:
                    return marks
                else:
                    print("Error: Marks must be between 0 and 100.")

            except ValueError:
                print("Error: Enter valid numeric marks.")

    def enter_existing_id(self, records, message, record_name):
        if not records:
            print("No", record_name, "records available.")
            return None

        while True:
            record_id = self.enter_text(message)

            if record_id in records:
                return record_id
            else:
                print("Error:", record_name, "not found. Try again.")

    def add_student(self):
        student_id = self.enter_unique_id(
            self.students, "Enter student ID: "
        )
        name = self.enter_text("Enter student name: ")
        age = self.enter_age()

        self.students[student_id] = Student(student_id, name, age)
        print("Student added successfully.")

    def add_faculty(self):
        faculty_id = self.enter_unique_id(
            self.faculty, "Enter faculty ID: "
        )
        name = self.enter_text("Enter faculty name: ")
        age = self.enter_age()
        subject = self.enter_text("Enter subject: ")
        salary = self.enter_salary()

        self.faculty[faculty_id] = Faculty(
            faculty_id, name, age, subject, salary
        )
        print("Faculty added successfully.")

    def add_course(self):
        course_id = self.enter_unique_id(
            self.courses, "Enter course ID: "
        )
        course_name = self.enter_text("Enter course name: ")

        while True:
            faculty_id = input(
                "Enter faculty ID (or press Enter for none): "
            ).strip()

            if faculty_id == "" or faculty_id in self.faculty:
                break
            else:
                print("Error: Faculty not found. Try again.")

        self.courses[course_id] = Course(
            course_id, course_name, faculty_id
        )
        print("Course added successfully.")

    def enroll_student(self):
        student_id = self.enter_existing_id(
            self.students, "Enter student ID: ", "Student"
        )

        if student_id is None:
            return

        course_id = self.enter_existing_id(
            self.courses, "Enter course ID: ", "Course"
        )

        if course_id is None:
            return

        student = self.students[student_id]

        if course_id in student.courses:
            print("Student is already enrolled.")
            return

        student.courses.append(course_id)
        print("Student enrolled successfully.")

    def enter_result(self):
        student_id = self.enter_existing_id(
            self.students, "Enter student ID: ", "Student"
        )

        if student_id is None:
            return

        course_id = self.enter_existing_id(
            self.courses, "Enter course ID: ", "Course"
        )

        if course_id is None:
            return

        student = self.students[student_id]

        if course_id not in student.courses:
            print("Student is not enrolled in this course.")
            return

        marks = self.enter_marks()
        student.results[course_id] = marks

        print("Result saved successfully.")

    def search_record(self):
        record_id = self.enter_text(
            "Enter student, faculty, or course ID: "
        )

        if record_id in self.students:
            student = self.students[record_id]
            student.display()

            print("Results:")

            if not student.results:
                print("No results available.")
            else:
                for course_id, marks in student.results.items():
                    course_name = self.courses[course_id].course_name
                    result = "Pass" if marks >= 40 else "Fail"
                    print(course_name, "-", marks, "-", result)

        elif record_id in self.faculty:
            self.faculty[record_id].display()

        elif record_id in self.courses:
            self.courses[record_id].display()

        else:
            print("Record not found.")

    def display_records(self):
        print("\n--- All Students ---")

        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                student.display()

        print("\n--- All Faculty ---")

        if not self.faculty:
            print("No faculty available.")
        else:
            for faculty in self.faculty.values():
                faculty.display()

        print("\n--- All Courses ---")

        if not self.courses:
            print("No courses available.")
        else:
            for course in self.courses.values():
                course.display()


def main():
    college = College()

    while True:
        print("\n===== College Management System =====")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Enter Student Result")
        print("6. Search Record")
        print("7. Display All Records")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            college.add_student()
        elif choice == "2":
            college.add_faculty()
        elif choice == "3":
            college.add_course()
        elif choice == "4":
            college.enroll_student()
        elif choice == "5":
            college.enter_result()
        elif choice == "6":
            college.search_record()
        elif choice == "7":
            college.display_records()
        elif choice == "8":
            print("Exiting College Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
