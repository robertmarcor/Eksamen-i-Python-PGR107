class Book:
    def __init__(self, title, author, num_pages, status):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.status = status # extra Attribute

    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"

    @classmethod
    def get_all_books(cls):
        """
        Creates and returns a list of Book objects for books, in this case the Harry Potter series.
        Each book is initialized with its title, author, number of pages,
        and availability status (True = available, False = checked out).
        
        Returns:
            list: A list containing all books as Book objects
        """
        return [
            cls("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223, True),
            cls("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 251, True),
            cls("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 317, True),
            cls("Harry Potter and the Goblet of Fire", "J.K. Rowling", 734, True),
            cls("Harry Potter and the Order of the Phoenix", "J.K. Rowling", 870, True),
            cls("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 652, True),
            cls("Harry Potter and the Deathly Hallows", "J.K. Rowling", 759, True)
        ]
