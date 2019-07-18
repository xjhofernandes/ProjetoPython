#from app import db
from werkzeug.security import check_password_hash

class User():

    def __init__(self): 
        self.id = None
        self._is_authenticated = False
        self._is_active = True
        self._is_anoymous = False

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
        