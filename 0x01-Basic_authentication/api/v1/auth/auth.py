#!/usr/bin/env python3
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
          -True: if path is not in list of strings
          -False: if path is in excluded_paths
        """
        if path is None:
            return True

        if excluded_paths is None:
            return True

        if path in excluded_paths:
            return False

        if path + '/' in excluded_paths:
            return False

        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization header
        Returns:
          - None: if request is None or no header key
          The value of the header request
        """
        if request is None:
            return None
        if request.headers is None:
            return None
        return request.headers.get("Authorization", None)
  

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        Returns: None
        """
        return None
