# Library Management System

This is a simple Library Management System implemented in Python. It allows users to manage books, users, and book checkouts within a library.

## Features

- **Book Management**: Add, update, delete, list, and search books by title, author, or ISBN.
- **User Management**: Add, update, delete, list, and search users by name or user ID.
- **Book Checkout**: Check out and check in books by users.
- **Logging**: All significant system events are logged to a file for auditing purposes.

### Classes and Methods

- **manage_book.BookStore**: Manages book-related operations such as adding, updating, deleting, listing, and searching for books.

- **manage_checkout.CheckoutStore**: Manages the checkout and check-in operations of books by users. It interacts with the BookManagement and UserManager objects to perform these operations.

- **manage_user.UserStore**: Manages user-related operations such as adding, updating, deleting, listing, and searching for users.

### Logging

Logging is implemented to record all significant system events. This aids in tracking system activities, debugging, and auditing purposes. Logs are stored in the 'log data' directory in the 'logging.txt' file.

# Classes
1. **Storage**: 
    * Responsible for handling file-based storage operations such as loading and saving data.
    * Methods:
        - load_data(): Loads data from the storage file.
        - save_data(data): Saves data to the storage file.

2. **Book**: 
    * Represents a book in the library.
    * Attributes:
        - title: Title of the book.
        - author: Author of the book.
        - isbn: ISBN (International Standard Book Number) of the book.
        - is_checked_out: Indicates whether the book is currently checked out.

    * Methods:
        - __init__(title, author, isbn): Initializes a new Book object.

3. **User**:
    * Represents a library user.
    * Attributes:
        - name: Name of the user.
        - user_id: Unique identifier for the user.
    * Methods:
        - __init__(name, user_id): Initializes a new User object.

4. **Library**:
    * Main class that manages books, users, and book transactions.
    * Attributes:
        - books: List of Book objects in the library.
        - users: List of User objects in the library.
        - checkouts: List of book checkout records.
        - storage: Storage object for handling data storage operations.
    * Methods:
        - load_data(): Loads data from storage into memory.
        - save_data(): Saves data from memory to storage.
        - Methods for managing books (add_book, update_book, delete_book, list_books, search_books).
        - Methods for managing users (add_user, update_user, delete_user, list_users, search_users).
        - Methods for book transactions (checkout_book, checkin_book, track_book_availability).
