def enter_marks():
    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input("Enter marks for subject " + str(i) + ": "))

                if mark < 0 or mark > 100:
                    print("Error: Marks must be between 0 and 100.")
                else:
                    marks.append(mark)
                    break

            except ValueError:
                print("Error: Please enter valid numeric marks.")

    return marks


def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5
    return total, percentage


def display_grade(percentage):
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 35:
        print("Grade: D")
    else:
        print("Grade: F")


def display_status(marks):
    if all(mark >= 35 for mark in marks):
        print("Status: Pass")
    else:
        print("Status: Fail")


def display_summary(marks):
    total, percentage = calculate_result(marks)

    print("\n--- Performance Summary ---")
    print("Total Marks :", total, "/ 500")
    print("Percentage  :", percentage, "%")
    print("Highest Mark:", max(marks))
    print("Lowest Mark :", min(marks))

    display_grade(percentage)
    display_status(marks)


def main():
    marks = []

    while True:
        print("\n--- Student Result Menu ---")
        print("1. Enter Marks")
        print("2. Calculate Result")
        print("3. Display Grade")
        print("4. Display Pass/Fail")
        print("5. Display Performance Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            marks = enter_marks()
            print("Marks entered successfully.")

        elif choice == "2":
            if marks:
                total, percentage = calculate_result(marks)
                print("Total Marks:", total, "/ 500")
                print("Percentage:", percentage, "%")
            else:
                print("Please enter marks first.")

        elif choice == "3":
            if marks:
                total, percentage = calculate_result(marks)
                display_grade(percentage)
            else:
                print("Please enter marks first.")

        elif choice == "4":
            if marks:
                display_status(marks)
            else:
                print("Please enter marks first.")

        elif choice == "5":
            if marks:
                display_summary(marks)
            else:
                print("Please enter marks first.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()