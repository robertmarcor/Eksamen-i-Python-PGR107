"""
Task 2 Library Management System

Program explanation:
2 Objects:
    - Library
    - Book

Library:
    - has a list of books and tracks the status of each book.
    - is responsible for adding, removing, checking in, and checking out books.
    - has functions for listing all books, checked in books, and checked out books.

Book:
    - Book has a title, author, number of pages, and status.
    - title is used to identify the book.
    - status is used to track if the book is checked in or checked out base on
        True = checked in
        False = checked out

Main Program:
    - creates a library object
    - adds all books to the library
    - displays a menu for the user to interact with.
    
    menu functions interact with the library object to add, remove, check in, and check out books.
    handles some validation and uses indexing to select books from the list to remove the need for typing out the title.
    
    has nice ascii menus and "fake" inputs/loading screens to make the program feel more interactive :)
"""
from Library import Library
from Book import Book
import os
import time

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def add_all_books(library):
    """Add all books to the library"""
    books = Book.get_all_books()
    print("Loading library data...")
    for book in books:
        library.add_book(book)
    print("✓ All books have been added to the library\n")
    time.sleep(1)
    
def checkin_menu(library):
    """Menu for checking in books"""
    clear_screen()
    print("\n═════════════════════════════════════")
    print("           RETURN A BOOK             ")
    print("═════════════════════════════════════")
    
    checked_out_books = library.list_checked_out_books()
    if not checked_out_books:
        input("\nPress Enter to return to the main menu...")
        return
    
    try:
        book_choice = int(input("\nBook number (0 to cancel): "))
        if book_choice == 0:
            print("\nReturn cancelled.")
            time.sleep(1)
            return
            
        if 1 <= book_choice <= len(checked_out_books):
            title = checked_out_books[book_choice - 1].title
            library.checkin_book(title)
        else:
            print("\n❌ Invalid book number")
    except ValueError:
        print("\n❌ Please enter a valid number")
        
    time.sleep(1)
    input("\nPress Enter to return to the main menu...")
    
def checkout_menu(library):
    """Menu for checking out books"""
    clear_screen()
    print("\n═════════════════════════════════════")
    print("           BORROW A BOOK             ")
    print("═════════════════════════════════════")
    
    checked_in_books = library.list_checked_in_books()
    if not checked_in_books:
        input("\nPress Enter to return to the main menu...")
        return
    
    try:
        book_choice = int(input("\nBook number (0 to cancel): "))
        if book_choice == 0:
            print("\nCheckout cancelled.")
            time.sleep(1)
            return
            
        if 1 <= book_choice <= len(checked_in_books):
            title = checked_in_books[book_choice - 1].title
            library.checkout_book(title)
        else:
            print("\n❌ Invalid book number")
    except ValueError:
        print("\n❌ Please enter a valid number")
        
    time.sleep(1)
    input("\nPress Enter to return to the main menu...")

def remove_book_menu(library):
    """Menu for removing books"""
    clear_screen()
    print("\n═════════════════════════════════════")
    print("      REMOVE A BOOK FROM LIBRARY     ")
    print("═════════════════════════════════════")
    
    checked_in_books = library.list_checked_in_books()
    if not checked_in_books:
        input("\nPress Enter to return to the main menu...")
        return
    
    try:
        book_choice = int(input("\nBook number (0 to cancel): "))
        if book_choice == 0:
            print("\nRemoval cancelled.")
            time.sleep(1)
            return
            
        if 1 <= book_choice <= len(checked_in_books):
            title = checked_in_books[book_choice - 1].title
            confirmation = input(f"\nAre you sure you want to remove '{title}'? (y/n): ")
            if confirmation.lower() == 'y':
                library.remove_book(title)
            else:
                print("\nRemoval cancelled.")
        else:
            print("\n❌ Invalid book number")
    except ValueError:
        print("\n❌ Please enter a valid number")
        
    time.sleep(1)
    input("\nPress Enter to return to the main menu...")

def view_all_books_menu(library):
    """Menu for viewing all books"""
    clear_screen()
    library.list_all_books()
    input("\nPress Enter to return to the main menu...")

def handle_menu_choice(library, choice):
    if choice == 1: # Check out book
        checkout_menu(library)
        return False
    elif choice == 2: # Check in book
        checkin_menu(library)
        return False
    elif choice == 3: # Remove book
        remove_book_menu(library)
        return False
    elif choice == 4: # List all books
        view_all_books_menu(library)
        return False
    elif choice == 5: # Exit
        print("\nThank you for using the Library Management System!")
        return True
    else:
        print("\n❌ Invalid choice. Please select a number between 1-5.")
        time.sleep(1)
        return False
    
    
if __name__ == "__main__":
    quit_app = False
    library = Library()
    
    # Welcome screen
    clear_screen()
    print("\n╔═══════════════════════════════════════╗")
    print("║      LIBRARY MANAGEMENT SYSTEM        ║")
    print("╚═══════════════════════════════════════╝")
    
    add_all_books(library)
    library.list_all_books()
    input("\nPress Enter to continue to the main menu...")
    
    # Main Loop
    while quit_app is False:
        clear_screen()
        print("\n╔═══════════════════════════════════════╗")
        print("║         LIBRARY MAIN MENU             ║")
        print("╚═══════════════════════════════════════╝")
        print("\n1. 📗 Borrow a book")
        print("2. 📕 Return a book")
        print("3. 🗑️  Remove a book from library")
        print("4. 📚 View all books")
        print("5. 👋 Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            quit_app = handle_menu_choice(library, choice)
        except ValueError:
            print("\n❌ Please enter a number.")
            time.sleep(1)
    

