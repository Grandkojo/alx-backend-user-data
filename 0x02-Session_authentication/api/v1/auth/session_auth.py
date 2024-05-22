#!/usr/bin/env python3
""" Session authentication
"""


from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ The session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session id for `user_id`
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
