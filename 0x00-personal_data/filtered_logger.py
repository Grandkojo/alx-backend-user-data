#!/usr/bin/env python3
"""This module contains the filtered_logger function."""

import re


def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """Returns a log message obfuscated."""
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
