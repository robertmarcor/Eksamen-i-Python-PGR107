class Library:
    list_of_books = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def remove_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                self.list_of_books.remove(book)
                print(f"\n✓ Book '{title}' has been removed from the library")
                return
        print(f"\n❌ Book '{title}' not found in library")

    def check_in(self, book):
        book.status = True

    def checkin_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                self.check_in(book)
                print(f"\n✓ Book '{title}' has been returned to the library")
                return
        print(f"\n❌ Book '{title}' not found in library")

    def check_out(self, book):
        book.status = False

    def checkout_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                self.check_out(book)
                print(f"\n✓ Book '{title}' has been checked out successfully")
                return
        print(f"\n❌ Book '{title}' not found in library")
        
        
    """ 
    Extra functions
    mostly for display purposes
    """
    def list_checked_in_books(self):
        # Books available for loan
        print("\n═════════════════════════════════════")
        print("       BOOKS AVAILABLE FOR LOAN       ")
        print("═════════════════════════════════════")
        
        checked_in = []
        for book in self.list_of_books:
            if book.status:
                checked_in.append(book)
                
        if checked_in:
            for i, book in enumerate(checked_in, 1):
                print(f"{i}. {book}")
            print("\nEnter the number of the book you want to select")
        else:
            print("No books available for loan at this time")
        print("─────────────────────────────────────")
        return checked_in
    
    def list_checked_out_books(self):
        # Books currently checked out
        print("\n═════════════════════════════════════")
        print("        BOOKS CURRENTLY ON LOAN       ")
        print("═════════════════════════════════════")
        
        checked_out = []
        for book in self.list_of_books:
            if not book.status:
                checked_out.append(book)
                
        if checked_out:
            for i, book in enumerate(checked_out, 1):
                print(f"{i}. {book}")
            print("\nEnter the number of the book you want to return")
        else:
            print("No books are currently checked out")
        print("─────────────────────────────────────")
        return checked_out
    
    def list_all_books(self):
        print("\n═════════════════════════════════════")
        print("      COMPLETE LIBRARY INVENTORY      ")
        print("═════════════════════════════════════")
        
        if self.list_of_books:
            for i, book in enumerate(self.list_of_books, 1):
                status = "📗 Available" if book.status else "📕 Checked out"
                print(f"{i}. {book} - {status}")
        else:
            print("The library is currently empty")
        print("─────────────────────────────────────")
  
        
