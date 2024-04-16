#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'

        # Check if the path is in the excluded_paths list
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

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
