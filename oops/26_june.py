
library = {
    "Python 101": True,
    "Harry Potter": True,
    "Data Science": True,
    "Machine Learning": True
}

def display_books():
    print("\nAvailable Books:")
    for book, available in library.items():
        status = "Available" if available else "Borrowed"
        print(f"- {book} [{status}]")
    print()


def add_book():
    book = input("Enter the name of the book to add: ")
    if book in library:
        print("That book already exists in the library.")
    else:
        library[book] = True
        print(f"'{book}' has been added to the library.")

def borrow_book():
    book = input("Enter the name of the book to borrow: ")
    if book in library:
        if library[book]:
            library[book] = False
            print(f"You have borrowed '{book}'. Please return it on time.")
        else:
            print(f"'{book}' is currently borrowed by someone else.")
    else:
        print("That book does not exist in the library.")

def return_book():
    book = input("Enter the name of the book to return: ")
    if book in library:
        if not library[book]:
            library[book] = True
            print(f"Thank you for returning '{book}'.")
        else:
            print(f"'{book}' was not borrowed.")
    else:
        print("That book does not belong to this library.")

def library_menu():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                display_books()
            elif choice == 2:
                add_book()
            elif choice == 3:
                borrow_book()
            elif choice == 4:
                return_book()
            elif choice == 5:
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

library_menu()
