#!/usr/bin/env python3
"""Basic Authentication
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic Auth class that imports from Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract the base64 auth header
        """
        if authorization_header is None or not \
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode the base64 auth string
        """
        if base64_authorization_header is None or not \
                isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header,
                                             validate=True)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, ValueError, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Returns the user email and password
        """
        if decoded_base64_authorization_header is None or not \
                isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        user_credentials = decoded_base64_authorization_header.split(':')
        user_name = user_credentials[0]
        password = user_credentials[1]
        return (user_name, password)
