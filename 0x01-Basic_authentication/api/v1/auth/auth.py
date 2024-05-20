#!/usr/bin/python3
"""the authentication class
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """the auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication
        Returns:
          - False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header
        Returns:
          - None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        Returns: None
        """
        return None
