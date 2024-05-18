#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """a function to hash passwords"""
    byte_str_password = bytes(password, 'utf-8')
    # print(byte_str_password)
    hashed = bcrypt.hashpw(byte_str_password, bcrypt.gensalt())
    return hashed
