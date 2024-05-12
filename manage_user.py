from storage import Storage 
from models import User 

class UserStore:
    def __init__(self):
        """
        Initialize the UserStore class.
        """
        self.storage = Storage('library data\\users.json')  # Initializing Storage with users data file path
        self.users = self.load_users()  # Loading users data from storage upon initialization

    def load_users(self):
        """
        Load users data from storage.
        """
        users_data = self.storage.load_data()  # Loading users data from storage
        return [User(**user) for user in users_data]  # Creating User objects from loaded data

    def save_users(self):
        """
        Save users data to storage.
        """
        users_data = [{'name': user.name, 'user_id': user.user_id} for user in self.users]  # Creating data to be saved
        self.storage.save_data(users_data)  # Saving users data to storage

    def add_user(self, name, user_id):
        """
        Add a new user.
        
        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier of the user.
        """
        new_user = User(name, user_id)  # Creating a new User object
        self.users.append(new_user)  # Adding the new user to the list
        self.save_users()  # Saving users data to storage

    def update_user(self, user_id, name=None):
        """
        Update user information.
        
        Args:
            user_id (str): The unique identifier of the user to be updated.
            name (str, optional): The new name of the user (if provided).
        
        Returns:
            bool: True if the user was successfully updated, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name  # Updating user's name if provided
                self.save_users()  # Saving updated users data to storage
                return True
        return False

    def delete_user(self, user_id):
        """
        Delete a user.
        
        Args:
            user_id (str): The unique identifier of the user to be deleted.
        
        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]  # Removing user from the list
                self.save_users()  # Saving updated users data to storage
                return True
        return False

    def list_users(self):
        """List all users."""
        for user in self.users:
            print("-"*60)
            print(f"Name: {user.name}, User ID: {user.user_id}")  # Displaying user information
            print("-"*60)

    def search_users(self, attribute, value):
        """
        Search for a user by attribute value.
        
        Args:
            attribute (str): The attribute to search by (e.g., 'name', 'user_id').
            value (str): The value of the attribute to search for.
        
        Returns:
            bool: True if the user was found, False otherwise.
        """
        for user in self.users:
            if getattr(user, attribute, '') == value:
                print("-"*25)
                print(f"  Name    : {user.name}")
                print(f"  User ID : {user.user_id}")  # Displaying user information
                print("-"*25)
                return True
        return False
