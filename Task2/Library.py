class Library:
    list_of_books = []
    checked_in_books = []
    checked_out_books = []

    def add_book(self, book):
        print(f"Adding book: {book}")
        self.list_of_books.append(book)

    def remove_book(self, title):
        print(f"Removing book: {title}")
        self.list_of_books.remove(title)

    def check_in(self, title):
        print(f"Checking in book: {title}")
        self.checked_in_books.append(title)

    def check_out(self, title):
        print(f"Checking out book: {title}")
        self.checked_out_books.append(title)
        
    """ Extra functions """
    def list_checked_in_books(self):
        # Checked in books
        print("=== Books checked in ===")
        if(len(self.checked_in_books) > 0):
            for book in self.checked_in_books:
                print(book)
        else:
            print("No books checked in")
        print("--------------------------------")        
        
    def list_checked_out_books(self):
        # Checked out books
        print("=== Books checked out ===")
        if(len(self.checked_out_books) > 0):
            for book in self.checked_out_books:
                print(book)
        else:
            print("No books checked out")
        print("--------------------------------")
    
    def list_all_books(self):
        print("=== Books in library ===")
        for book in self.list_of_books:
            print(book)
        print("--------------------------------")
    

        

    
        
