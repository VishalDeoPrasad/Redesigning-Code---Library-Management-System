from storage import Storage

class CheckoutStore:
    def __init__(self, book_manager, user_manager):
        # Initialize the CheckoutStore with a Storage object to handle data persistence,
        # a book_manager to manage books, and a user_manager to manage users.
        self.storage = Storage('library data\\checkouts.json')
        self.book_manager = book_manager
        self.user_manager = user_manager
        # Load existing checkouts from storage when initializing the CheckoutStore.
        self.checkouts = self.load_checkouts()

    def checkout_book(self, user_id, isbn):
        # Attempt to find the book with the provided ISBN in the book_manager's collection.
        for book in self.book_manager.books:
            # If the book is found and is available for checkout, mark it as checked out,
            # add a checkout record, save the updated book data, and save the checkout records.
            if book.isbn == isbn and not book.is_checked_out:
                book.is_checked_out = True
                self.checkouts.append({"user_id": user_id, "isbn": isbn})
                self.book_manager.save_books()
                self.save_checkouts()
                return True
        # If the book is not found or is already checked out, return False to indicate failure.
        return False

    def checkin_book(self, isbn):
        # Attempt to find the book with the provided ISBN in the book_manager's collection.
        for book in self.book_manager.books:
            # If the book is found and is currently checked out, mark it as checked in,
            # remove its checkout record, save the updated book data, and save the checkout records.
            if book.isbn == isbn and book.is_checked_out:
                book.is_checked_out = False
                self.checkouts = [checkout for checkout in self.checkouts if checkout['isbn'] != isbn]
                self.book_manager.save_books()
                self.save_checkouts()
                return True
        # If the book is not found or is not checked out, return False to indicate failure.
        return False

    def load_checkouts(self):
        # Load checkout records from storage.
        return self.storage.load_data()

    def save_checkouts(self):
        # Save checkout records to storage.
        self.storage.save_data(self.checkouts)
