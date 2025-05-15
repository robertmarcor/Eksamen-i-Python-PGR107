class Library:
    list_of_books = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def remove_book(self, title):
        self.list_of_books.remove(title)

    def check_in(self, title):
        self.list_of_books.append(title)

    def check_out(self, title):
        self.list_of_books.remove(title)
        
