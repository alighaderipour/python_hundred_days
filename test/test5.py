class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append("title")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title == title]

    def check_in(self, title):
        self.books = next()
