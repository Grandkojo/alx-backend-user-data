#!/usr/bin/env python3
""" Session authentication
"""


from api.v1.auth.auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User id based on session id
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> str:
        """ returns a user instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        user_id_for_session = self.user_id_for_session_id(session_id)
        return User.get(user_id_for_session)

    def destroy_session(self, request=None) -> str:
        """ destroy the user session
        """
        if request is None or self.session_cookie(request) is None:
            return False
        user_session = self.session_cookie(request)
        if self.user_id_for_session_id(user_session) is None:
            return False
        del self.user_id_by_session_id[user_session]
        return True
