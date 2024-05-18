#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """a function to hash passwords"""
    byte_str_password = b"f'{password}'"
    hashed = bcrypt.hashpw(byte_str_password, bcrypt.gensalt())
    # if bcrypt.checkpw(byte_str_password, hashed):
        # print('It matches')
    return hashed
