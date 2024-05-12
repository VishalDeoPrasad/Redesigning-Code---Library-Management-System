import manage_user
import manage_book
import manage_checkout
import datetime
import logging

# Configure logging with levels and format
logging.basicConfig(filename='log data\\logging.txt', level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

def menu():
    print("\nWelcome to the Library Management System!")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Check out a Book")
    print("4. Check in a Book")
    print("5. View book availability")
    print("6. View System Logging")
    print("7. Exit")
    choice = input("Enter your choice: ")
    return choice

def read_logging(log_file):
    log_entries = []
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split(' : ')
            date_str, level, message = parts[0], parts[1], parts[2].strip()
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S,%f')
            log_entry = {
                'date': date,
                'level': level.strip(),
                'message': message
            }
            log_entries.append(log_entry)
    return log_entries

def manage_books(book_manager):
    while True:
        print("\nBook Management:")
        print("1. Add a New Book")
        print("2. Update Book Details")
        print("3. Remove a Book")
        print("4. View Book List")
        print("5. Search Books")
        print("6. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            # Check if the book with the given ISBN already exists
            if book_manager.is_isbn_unique(isbn):
                book_manager.add_book(title, author, isbn)
                print("Book added successfully.")
                logging.info(f"Book added: Title: {title}, Author: {author}, ISBN: {isbn}")
            else:
                print("A book with this ISBN already exists.")
                logging.info(f"This ISBN already exists: Title: {title}, Author: {author}, ISBN: {isbn}")

        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep unchanged): ")
            author = input("Enter new author (leave blank to keep unchanged): ")
            # Proceed with update if the book exists
            if book_manager.does_book_exist(isbn):
                updated = book_manager.update_book(isbn, title if title else None, author if author else None)
                if updated:
                    print("Book updated successfully.")
                    logging.info(f"Book updated successfully: Title: {title}, Author: {author}, ISBN: {isbn}")
                else:
                    print("Another book with the same title or author already exists.")
                    logging.info(f"Another book with the same title or author already exists: Title: {title}, Author: {author}")
            else:
                print("Book not found.")
                logging.info(f"Book not found.")

        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            if book_manager.delete_book(isbn):
                print("Book deleted successfully.")
                logging.info(f"Book deleted successfully.")
            else:
                print("Book not found.")
                logging.info(f"Book not found with ISBN:{isbn}")
                

        elif choice == '4':
            book_manager.list_books()
            logging.info(f"Display All Books...")
            
        elif choice == '5':
            attribute = input("Search by (title/author/isbn): ")
            value = input(f"Enter {attribute}: ")
            if not book_manager.search_books(attribute, value):
                print("No books found.")
                logging.info(f"Book not found with {value}")
            else:
                logging.info(f"Search Successfully happen with (title/author/isbn): {value}")
        elif choice == '6':
            break

def manage_users(user_manager):
    while True:
        print("\nUser Management:")
        print("1. Add a New User")
        print("2. Update User Information")
        print("3. Remove a User")
        print("4. View User List")
        print("5. Search Users")
        print("6. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            print("User added successfully.")
            logging.info(f"User added successfully. name: {name}, user_id: {user_id} ")

        elif choice == '2':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name: ")
            updated = user_manager.update_user(user_id, name)
            if updated:
                print("User updated successfully.")
                logging.info(f"User updated successfully. name: {name}, user_id: {user_id} ")
            else:
                print("User not found.")
                logging.info(f"User not found")

        elif choice == '3':
            user_id = input("Enter user ID of the user to delete: ")
            if user_manager.delete_user(user_id):
                print("User deleted successfully.")
                logging.info(f"User Delete successfully. user_id: {user_id}")
            else:
                print("User not found.")
                logging.info(f"Can't delete user. User not found")

        elif choice == '4':
            user_manager.list_users()

        elif choice == '5':
            attribute = input("Search by (name/user_id): ")
            value = input(f"Enter {attribute}: ")
            if not user_manager.search_users(attribute, value):
                print("No users found.")
                logging.info(f"Can't search user. User not found")

        elif choice == '6':
            break

def main():
    bm = manage_book.BookStore()
    um = manage_user.UserStore()
    cm = manage_checkout.CheckoutStore(bm, um)

    while True:
        choice = menu()

        if choice == '1':
            manage_books(bm)

        elif choice == '2':
            manage_users(um)

        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            if cm.checkout_book(user_id, isbn):
                print("Book checked out successfully.")
                logging.info(f"Book checked out successfully. user_id: {user_id}, isbn:{isbn}")
            else:
                print("Failed to checkout book. It might be already checked out or does not exist.")
                logging.info(f"Book not found with this user_id: {user_id}, isbn:{isbn}")

        elif choice == '4':
            isbn = input("Enter ISBN of the book to check-in: ")
            if cm.checkin_book(isbn):
                print("Book checked in successfully.")
                logging.info(f"Book checked in successfully. isbn:{isbn}")
            else:
                print("Failed to check in book. It might not be checked out or does not exist.")
                logging.info(f"Failed to check in book. It might not be checked out or does not exist. isbn:{isbn}")

        elif choice == '5':
            print("Track book availability")
            result = bm.track_book()
            print("Total Number of Books: ", len(result))

            input_isbn = input("Enter ISBN of the book to Track book availability: ")
            ans = False
            for book in result:
                #print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Available' if not book.is_checked_out else 'Not Available'}")
                if book.isbn == input_isbn:
                    print("-"*35)
                    print(f"  Title     : {book.title}")
                    print(f"  Author    : {book.author}")
                    print(f"  ISBN      : {book.isbn}")
                    print(f"  Available : {'Available' if not book.is_checked_out else 'Not Available'}")
                    print("-"*35)
                    #print(book.title, "-->", "Available" if not book.is_checked_out else "Not Available")
                    logging.info(f"Track book availability. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available:{'Available' if not book.is_checked_out else 'Not Available'}")
                    ans = True
                    break

            if ans == False:
                print("Try Again, Please Check ISBN...")
                logging.info(f"Try Again, Please Check ISBN...")

        elif choice == '6':
            # Example usage:
            log_file = 'log data\\logging.txt'
            logs = read_logging(log_file)
            for log in logs:
                print(log)

        elif choice == '7':
            print("Exiting Library Management System.")
            logging.info("Application exited successfully...")
            break

        else:
            logging.info("Invalid Choice Entered...")
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()
