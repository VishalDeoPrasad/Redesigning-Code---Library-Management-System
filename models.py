class Book:
    def __init__(self, title, author, isbn, is_checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
