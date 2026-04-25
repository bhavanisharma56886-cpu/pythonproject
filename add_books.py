from utils import books

def add_book():
    print("\n========== ADD NEW BOOK ==========")

    while True:
        book_name = input("Enter Book Name: ").upper()

        if book_name in books:
            print("⚠ Book already exists.")
        else:
            books[book_name] = "available"   # same work like append()
            print(f"✅ Book '{book_name}' added successfully.")

        choice = input("Do you want to add another book? (yes/no): ").lower()

        if choice != "yes":
            break

        

        
        
        
        
        