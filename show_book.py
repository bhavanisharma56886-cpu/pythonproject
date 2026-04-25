from utils import books

def show_books():
    print("\n========== ALL BOOKS ==========")

    if len(books) == 0:
        print("No books available.")
        return

    for book, details in books.items():
        print("\n----------------------")
        print(f"Book Name    : {book}")
        print(f"Status       : {details['status']}")

        if details["status"] == "issued":
            print(f"Student Name : {details['student_name']}")
            print(f"Issue Date   : {details['issue_date']}")
            print(f"Days         : {details['days']}")