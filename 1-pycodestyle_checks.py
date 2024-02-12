#!/usr/bin/python3

class Book:
    """
    Represents a book in the library catalog.
    """
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}"


class LibraryCatalog:
    """
    Represents a library catalog.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library catalog.

        Args:
            book (Book): The book object to add.
        """
        self.books.append(book)

    def search_by_title(self, title):
        """
        Search for a book by title.

        Args:
            title (str): The title of the book to search for.

        Returns:
            list: A list of books matching the title.
        """
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                matching_books.append(book)
        return matching_books

    def search_by_author(self, author):
        """
        Search for books by author.

        Args:
            author (str): The author's name to search for.

        Returns:
            list: A list of books written by the author.
        """
        matching_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                matching_books.append(book)
        return matching_books

    def search_by_isbn(self, isbn):
        """
        Search for a book by ISBN.

        Args:
            isbn (str): The ISBN of the book to search for.

        Returns:
            list: A list of books matching the ISBN.
        """
        matching_books = []
        for book in self.books:
            if book.isbn == isbn:
                matching_books.append(book)
        return matching_books


if __name__ == "__main__":
    # Example of code implimentation
    library = LibraryCatalog()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
    book3 = Book("1984", "George Orwell", "978-0451524935")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Books by Harper Lee:")
    for book in library.search_by_author("Harper Lee"):
        print(book)

    print("\nBooks with '1984' in the title:")
    for book in library.search_by_title("1984"):
        print(book)
