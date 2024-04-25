#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ hash password method"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate UUIDs"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """init method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            existing_user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            new_user = self._db.add_user(email, pwd)
            return new_user
        else:
            raise ValueError('User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """credentials validation, return a boolean"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode('utf-8'),
                                  hashed_password=user.hashed_password)

    def create_session(self, email: str) -> str:
        """returns session id as a string"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
