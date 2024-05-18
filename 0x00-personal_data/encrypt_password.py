#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """a function to hash passwords"""
    byte_str_password = bytes(password, 'utf-8')
    # print(byte_str_password)
    hashed = bcrypt.hashpw(byte_str_password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if the hashed_password and password matches"""
    bytes_str_password = bytes(password, 'utf-8')
    if bcrypt.checkpw(bytes_str_password, hashed_password):
        return True
    return False
