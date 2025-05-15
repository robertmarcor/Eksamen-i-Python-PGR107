from Library import Library
from Book import Book
import time
from utils import clear_screen

def test_script():
    clear_screen()
    print("\n═════════════════════════════════════")
    print("          AUTOMATIC TEST MODE         ")
    print("═════════════════════════════════════")
    
    test_library = Library()
    print("\n1. Creating a new test library...")
    time.sleep(1)
    
    print("\n2. Adding books to the test library...")
    lotr_books = [
        Book("The Fellowship of the Ring", "J.R.R. Tolkien", 423, True),
        Book("The Two Towers", "J.R.R. Tolkien", 352, True),
        Book("The Return of the King", "J.R.R. Tolkien", 416, True),
        Book("The Hobbit", "J.R.R. Tolkien", 310, True),
        Book("The Silmarillion", "J.R.R. Tolkien", 365, True)
    ]
    
    for book in lotr_books:
        test_library.add_book(book)
        print(f"   Added: {book}")
        time.sleep(0.5)
    
    test_book_title = "The Fellowship of the Ring"
    test_remove_book_title = "The Silmarillion"
    
    # Check out a book using the title variable
    print(f"\n3. Checking out '{test_book_title}'...")
    time.sleep(1)
    test_library.checkout_book(test_book_title)
    
    # Return a book using the title variable
    print(f"\n4. Returning '{test_book_title}'...")
    time.sleep(1)
    test_library.checkin_book(test_book_title)
    
    # Remove a book
    print(f"\n5. Removing '{test_remove_book_title}' from the library...")
    time.sleep(1)
    test_library.remove_book(test_remove_book_title)
    
    # Display all books to verify results
    print("\n6. Displaying all books in the test library:")
    time.sleep(1)
    test_library.list_all_books()
    
    print("\nAutomatic test completed!")
    input("\nPress Enter to return to the main menu...") 