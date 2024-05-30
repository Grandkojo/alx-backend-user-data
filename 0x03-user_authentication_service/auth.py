#!/usr/bin/env python3
""" A hashed password
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a user based on email and password
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exits'.format(email))
        except NoResultFound:
            pass
        user_password = _hash_password(password)
        user= self._db.add_user(email, user_password)

def _hash_password(password: str) -> bytes:
    """ returns a hashed password in bytes
    """
    byte_password = password.encode('utf-8')
    return bcrypt.hashpw(byte_password, bcrypt.gensalt())
