"""
Task 2 Library Management System

Program explanation:
2 Objects:
    - Library
    - Book

Library has a list of books.
Book has a title, author, and number of pages.

Library is responsible for adding, removing, and checking out books.
Book is for storing the book's title, author, and number of pages.


"""
from Library import Library
from Book import Book

def add_all_books(library):
    books = Book.get_harry_potter_books()
    for book in books:
        library.add_book(book)
    print("All books added to library\n")

def handle_menu_choice(library, choice):
    if choice == 1: # Check out book
        if(len(library.list_of_books) <= 0):
            print("There are no books to be checked out")
            return False
        else:
            title = input("Enter the title of the book to check out: ")
            library.check_out(title)
            return False
    elif choice == 2: # Check in book
        if(len(library.checked_out_books) <= 0):
            print("There are no books to be checked in")
            return False
        else:
            title = input("Enter the title of the book to check in: ")
            library.check_in(title) 
            return False
    elif choice == 3: # Remove book
        title = input("Enter the title of the book to remove: ")
        library.remove_book(title)
        return False
    elif choice == 4: # List all books
        library.list_all_books()
        library.list_checked_in_books()
        library.list_checked_out_books()
        return False
    elif choice == 5:
        print("Exiting program...")
        return True
    else:
        print("Invalid choice. Please try again.")
        return False

if __name__ == "__main__":
    quit_app = False
    library = Library()
    print("=== Library App ===")
    add_all_books(library)
    library.list_all_books()
    library.list_checked_in_books()
    library.list_checked_out_books()
    
    # Main Loop
    while quit_app is False:
        print("=== Library Menu ===")
        print("1. Check out book")
        print("2. Check in book")
        print("3. Remove a book")
        print("4. List all books")
        print("5. Exit")
        try:
            valid_choice = "12345"
            choice = int(input("Enter your choice: "))
            quit_app = handle_menu_choice(library, choice)
        except ValueError:
            print("Please enter a number.")
    

