from add_books import add_book
from issue_books import issue_book
from return_book import return_book
from show_book import show_books

while True:
    print("\n==============================")
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("==============================")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        show_books()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")