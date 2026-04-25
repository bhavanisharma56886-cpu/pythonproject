from utils import books

def return_book():
    print("\n========== RETURN BOOK ==========")

    book_name = input("Enter Book Name: ").upper()

    if book_name not in books:
        print("❌ Invalid Book Name")
        return

    if books[book_name]["status"] == "available":
        print("⚠ This book was not issued")
        return

    allotted_days = books[book_name]["days"]
    used_days = int(input("Enter total days used: "))

    fine = 0

    if used_days > allotted_days:
        extra_days = used_days - allotted_days

        for day in range(1, extra_days + 1):
            week = (day - 1) // 7 + 1
            fine += 10 * week

        print(f"⚠ Late Return Fine = ₹{fine}")
    else:
        print("✅ Returned on time. No Fine.")

    books[book_name]["status"] = "available"
    books[book_name]["student_name"] = ""
    books[book_name]["issue_date"] = ""
    books[book_name]["days"] = 0

    print(f"📘 Book '{book_name}' returned successfully.")