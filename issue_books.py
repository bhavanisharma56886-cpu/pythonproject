from utils import books
from datetime import datetime

def issue_book():
    print("\n========== ISSUE BOOK ==========")

    book_name = input("Enter Book Name: ").upper()

    if book_name not in books:
        print("❌ Book not found.")
        return

    if books[book_name]["status"] == "issued":
        print("⚠ Book already issued.")
        return

    student_name = input("Enter Student Name: ")
    days = int(input("Enter number of days: "))

    issue_date = datetime.now().strftime("%d-%m-%Y")

    books[book_name]["status"] = "issued"
    books[book_name]["student_name"] = student_name
    books[book_name]["issue_date"] = issue_date
    books[book_name]["days"] = days

    print("\n✅ Book Issued Successfully")
    print(f"Book Name    : {book_name}")
    print(f"Student Name : {student_name}")
    print(f"Issue Date   : {issue_date}")
    print(f"Days         : {days}")

    print("\nFine Rules:")
    print("1st Week → ₹10/day")
    print("2nd Week → ₹20/day")
    print("3rd Week → ₹30/day")