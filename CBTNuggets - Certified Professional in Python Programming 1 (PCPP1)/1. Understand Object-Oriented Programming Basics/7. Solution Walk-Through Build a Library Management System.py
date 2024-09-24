class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    # def __str__(self):
    #     return f"'{self.title}' by {self.author} - Pages: {self.year}, Status: {self.status}"

    def __repr__(self):
        return f"'{self.title}' by {self.author} - Pages: {self.year}, Status: {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def check_in(self, title):
        book = next((book for book in self.books if book.title == title), None)
        if book is not None:
            book.status = "available"

    def check_out(self, title):
        book = next((book for book in self.books if book.title == title), None)
        if book is not None:
            book.status = "borrowed"

    def display_books(self):
        for book in self.books:
            print(book)


the_alchemist = Book("Alchemist", "Paulo Coelho", 2008, "available")
my_library = Library()
my_library.add_book(the_alchemist)
my_library.add_book(
    Book(title="Blindness", author="José Saramago", year=1995, status="available")
)
my_library.display_books()
