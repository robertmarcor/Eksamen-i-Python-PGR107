class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.num_pages} pages)"

    @classmethod
    def get_harry_potter_books(cls):
        return [
            cls("Philosopher's Stone", "J.K. Rowling", 223),
            cls("Chamber of Secrets", "J.K. Rowling", 251),
            cls("Prisoner of Azkaban", "J.K. Rowling", 317),
            cls("Goblet of Fire", "J.K. Rowling", 734),
            cls("Order of the Phoenix", "J.K. Rowling", 870),
            cls("Half-Blood Prince", "J.K. Rowling", 652),
            cls("Deathly Hallows", "J.K. Rowling", 759)
        ]
