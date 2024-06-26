#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authorithation """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request"""
        if request is None:
            return None

        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user based on the request"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
