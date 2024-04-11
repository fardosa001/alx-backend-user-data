#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = r'({})[^{}]+'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1{}'.format(redaction), message)
