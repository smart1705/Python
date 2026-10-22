LibraryManagement/
storage.py
books.py
members.py
transactions.py
reports.py
main.py



File 1: storage.py
import json
import os


def load_data(filename):
    if not os.path.exists(filename):
        if save_data(filename, []):
            return []
        return None

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Invalid data format in", filename)
            return None

        return data

    except (json.JSONDecodeError, OSError):
        print("Error reading file:", filename)
        return None


def save_data(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except (OSError, TypeError):
        print("Error saving file:", filename)
        return False


def enter_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text
        else:
            print("Error: This field cannot be empty.")


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


File 2: books.py
from storage import load_data, save_data, enter_text

FILE_NAME = "books40.json"


def add_book():
    books = load_data(FILE_NAME)

    if books is None:
        return

    while True:
        book_id = enter_text("Enter Book ID: ")

        if any(book["Book ID"] == book_id for book in books):
            print("Error: Book ID already exists!")
        else:
            break

    title = enter_text("Enter Title: ")
    author = enter_text("Enter Author: ")
    category = enter_text("Enter Category: ")

    book = {
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Category": category,
        "Available": True,
        "Member ID": ""
    }

    books.append(book)

    if save_data(FILE_NAME, books):
        print("Book added successfully!")


def search_book():
    books = load_data(FILE_NAME)

    if books is None:
        return

    book_id = enter_text("Enter Book ID: ")

    for book in books:
        if book["Book ID"] == book_id:
            print(book)
            return

    print("Book not found!")


def update_book():
    books = load_data(FILE_NAME)

    if books is None:
        return

    book_id = enter_text("Enter Book ID to update: ")

    for book in books:
        if book["Book ID"] == book_id:
            title = enter_text("Enter new Title: ")
            author = enter_text("Enter new Author: ")
            category = enter_text("Enter new Category: ")

            book["Title"] = title
            book["Author"] = author
            book["Category"] = category

            if save_data(FILE_NAME, books):
                print("Book updated successfully!")
            return

    print("Book not found!")


def display_books():
    books = load_data(FILE_NAME)

    if books is None:
        return

    if not books:
        print("No books available.")
        return

    for book in books:
        print(book)


File 3: members.py
from storage import load_data, save_data, enter_text

FILE_NAME = "members40.json"


def add_member():
    members = load_data(FILE_NAME)

    if members is None:
        return

    while True:
        member_id = enter_text("Enter Member ID: ")

        if any(member["Member ID"] == member_id for member in members):
            print("Error: Member ID already exists!")
        else:
            break

    name = enter_text("Enter Name: ")
    course = enter_text("Enter Course: ")
    phone = enter_text("Enter Phone: ")
    email = enter_text("Enter Email: ")

    member = {
        "Member ID": member_id,
        "Name": name,
        "Course": course,
        "Phone": phone,
        "Email": email
    }

    members.append(member)

    if save_data(FILE_NAME, members):
        print("Member added successfully!")


def search_member():
    members = load_data(FILE_NAME)

    if members is None:
        return

    member_id = enter_text("Enter Member ID: ")

    for member in members:
        if member["Member ID"] == member_id:
            print(member)
            return

    print("Member not found!")


def update_member():
    members = load_data(FILE_NAME)

    if members is None:
        return

    member_id = enter_text("Enter Member ID to update: ")

    for member in members:
        if member["Member ID"] == member_id:
            name = enter_text("Enter new Name: ")
            course = enter_text("Enter new Course: ")
            phone = enter_text("Enter new Phone: ")
            email = enter_text("Enter new Email: ")

            member["Name"] = name
            member["Course"] = course
            member["Phone"] = phone
            member["Email"] = email

            if save_data(FILE_NAME, members):
                print("Member updated successfully!")
            return

    print("Member not found!")


def display_members():
    members = load_data(FILE_NAME)

    if members is None:
        return

    if not members:
        print("No members available.")
        return

    for member in members:
        print(member)


File 4: transactions.py
from storage import load_data, save_data, enter_text

BOOK_FILE = "books40.json"
MEMBER_FILE = "members40.json"
TRANSACTION_FILE = "transactions40.json"


def issue_book():
    books = load_data(BOOK_FILE)
    members = load_data(MEMBER_FILE)
    transactions = load_data(TRANSACTION_FILE)

    if books is None or members is None or transactions is None:
        return

    if not books:
        print("No books available.")
        return

    if not members:
        print("No members registered.")
        return

    while True:
        book_id = enter_text("Enter Book ID: ")
        book = None

        for item in books:
            if item["Book ID"] == book_id:
                book = item
                break

        if book is not None:
            break

        print("Book not found. Try again.")

    if not book["Available"]:
        print("Book is already issued!")
        return

    while True:
        member_id = enter_text("Enter Member ID: ")
        member_found = False

        for member in members:
            if member["Member ID"] == member_id:
                member_found = True
                break

        if member_found:
            break

        print("Member not found. Try again.")

    book["Available"] = False
    book["Member ID"] = member_id

    transactions.append({
        "Book ID": book_id,
        "Member ID": member_id,
        "Status": "Issued"
    })

    if not save_data(BOOK_FILE, books):
        return

    if save_data(TRANSACTION_FILE, transactions):
        print("Book issued successfully!")


def return_book():
    books = load_data(BOOK_FILE)
    transactions = load_data(TRANSACTION_FILE)

    if books is None or transactions is None:
        return

    if not books:
        print("No books available.")
        return

    while True:
        book_id = enter_text("Enter Book ID to return: ")
        book = None

        for item in books:
            if item["Book ID"] == book_id:
                book = item
                break

        if book is not None:
            break

        print("Book not found. Try again.")

    if book["Available"]:
        print("Book is not currently issued!")
        return

    member_id = book["Member ID"]

    book["Available"] = True
    book["Member ID"] = ""

    for transaction in reversed(transactions):
        if (
            transaction["Book ID"] == book_id
            and transaction["Status"] == "Issued"
        ):
            transaction["Status"] = "Returned"
            break

    if not save_data(BOOK_FILE, books):
        return

    if save_data(TRANSACTION_FILE, transactions):
        print("Book returned successfully!")
        print("Previously issued to:", member_id)


def display_transactions():
    transactions = load_data(TRANSACTION_FILE)

    if transactions is None:
        return

    if not transactions:
        print("No transactions available.")
        return

    for transaction in transactions:
        print(transaction)



File 5: reports.py
from storage import load_data, enter_text

FILE_NAME = "books40.json"


def available_books():
    books = load_data(FILE_NAME)

    if books is None:
        return

    found = False
    print("\n--- Available Books ---")

    for book in books:
        if book["Available"]:
            print(book)
            found = True

    if not found:
        print("No available books found.")


def issued_books():
    books = load_data(FILE_NAME)

    if books is None:
        return

    found = False
    print("\n--- Issued Books ---")

    for book in books:
        if not book["Available"]:
            print(book)
            found = True

    if not found:
        print("No issued books found.")


def books_by_category():
    books = load_data(FILE_NAME)

    if books is None:
        return

    category = enter_text("Enter Category: ")
    found = False

    for book in books:
        if book["Category"].casefold() == category.casefold():
            print(book)
            found = True

    if not found:
        print("No books found in this category.")


def books_by_member():
    books = load_data(FILE_NAME)

    if books is None:
        return

    member_id = enter_text("Enter Member ID: ")
    found = False

    for book in books:
        if (
            not book["Available"]
            and book["Member ID"].casefold() == member_id.casefold()
        ):
            print(book)
            found = True

    if not found:
        print("No books issued to this member.")


def total_books():
    books = load_data(FILE_NAME)

    if books is not None:
        print("Total number of books:", len(books))
File 6: main.py
import books
import members
import transactions
import reports


def book_menu():
    while True:
        print("\n--- Book Management ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Update Book")
        print("4. Display Books")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            books.add_book()
        elif choice == "2":
            books.search_book()
        elif choice == "3":
            books.update_book()
        elif choice == "4":
            books.display_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")


def member_menu():
    while True:
        print("\n--- Member Management ---")
        print("1. Add Member")
        print("2. Search Member")
        print("3. Update Member")
        print("4. Display Members")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            members.add_member()
        elif choice == "2":
            members.search_member()
        elif choice == "3":
            members.update_member()
        elif choice == "4":
            members.display_members()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")


def report_menu():
    while True:
        print("\n--- Library Reports ---")
        print("1. Available Books")
        print("2. Issued Books")
        print("3. Books by Category")
        print("4. Books by Member")
        print("5. Total Books")
        print("6. All Transactions")
        print("7. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            reports.available_books()
        elif choice == "2":
            reports.issued_books()
        elif choice == "3":
            reports.books_by_category()
        elif choice == "4":
            reports.books_by_member()
        elif choice == "5":
            reports.total_books()
        elif choice == "6":
            transactions.display_transactions()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Try again.")


def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            book_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            transactions.issue_book()
        elif choice == "4":
            transactions.return_book()
        elif choice == "5":
            report_menu()
        elif choice == "6":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()