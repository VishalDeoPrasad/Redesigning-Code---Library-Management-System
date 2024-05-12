from storage import Storage  
from models import Book  

class BookStore:
    def __init__(self):
        """
        Initialize the BookStore class.
        """
        self.storage = Storage('library data\\books.json')  # Initializing Storage with books data file path
        self.books = self.load_books()  # Loading books data from storage upon initialization

    def add_book(self, title, author, isbn):
        """
        Add a new book.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        # Assume uniqueness check is done prior
        new_book = Book(title, author, isbn)  # Creating a new Book object
        self.books.append(new_book)  # Adding the new book to the list
        self.save_books()  # Saving books data to storage

    def load_books(self):
        """
        Load books data from storage.
        """
        books_data = self.storage.load_data()  # Loading books data from storage
        return [Book(**book) for book in books_data]  # Creating Book objects from loaded data

    def track_book(self):
        """
        Track book availability.
        
        Returns:
            list: List of all books.
        """
        return self.books

    def update_book(self, isbn, title=None, author=None):
        """
        Update book information.
        
        Args:
            isbn (str): The ISBN of the book to be updated.
            title (str, optional): The new title of the book (if provided).
            author (str, optional): The new author of the book (if provided).
        
        Returns:
            bool: True if the book was successfully updated, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title  # Updating book's title if provided
                if author:
                    book.author = author  # Updating book's author if provided
                self.save_books()  # Saving updated books data to storage
                return True
        return False

    def delete_book(self, isbn):
        """
        Delete a book.
        
        Args:
            isbn (str): The ISBN of the book to be deleted.
        
        Returns:
            bool: True if the book was successfully deleted, False otherwise.
        """
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]  # Removing book from the list
                self.save_books()  # Saving updated books data to storage
                return True
        return False

    def list_books(self):
        """List all books."""
        for book in self.books:
            print("-"*75)
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Yes' if not book.is_checked_out else 'No'}")
            print("-"*75)

    def search_books(self, attribute, value):
        """
        Search for a book by attribute value.
        
        Args:
            attribute (str): The attribute to search by (e.g., 'title', 'author', 'isbn').
            value (str): The value of the attribute to search for.
        
        Returns:
            bool: True if the book was found, False otherwise.
        """
        for book in self.books:
            if getattr(book, attribute, '') == value:
                print("-"*25)
                print(f"  Title  : {book.title}")
                print(f"  Author : {book.author}")
                print(f"  ISBN   : {book.isbn}")
                print("-"*25)
                return True
        return False

    def save_books(self):
        """
        Save books data to storage.
        """
        books_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'is_checked_out': book.is_checked_out} for book in self.books]
        self.storage.save_data(books_data)

    def is_isbn_unique(self, isbn):
        """
        Check if the ISBN of a book is unique.
        
        Args:
            isbn (str): The ISBN of the book.
        
        Returns:
            bool: True if the ISBN is unique, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                return False
        return True

    def does_book_exist(self, isbn):
        """
        Check if a book exists.
        
        Args:
            isbn (str): The ISBN of the book.
        
        Returns:
            bool: True if the book exists, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                return True
        return False

    def is_title_unique(self, title, isbn):
        """
        Check if the title of a book is unique.
        
        Args:
            title (str): The title of the book.
            isbn (str): The ISBN of the book (to exclude from comparison).
        
        Returns:
            bool: True if the title is unique, False otherwise.
        """
        for book in self.books:
            if book.title == title and book.isbn != isbn:
                return False
        return True

    def is_author_unique(self, author, isbn):
        """
        Check if the author of a book is unique.
        
        Args:
            author (str): The author of the book.
            isbn (str): The ISBN of the book (to exclude from comparison).
        
        Returns:
            bool: True if the author is unique, False otherwise.
        """
        for book in self.books:
            if book.author == author and book.isbn != isbn:
                return False
        return True
