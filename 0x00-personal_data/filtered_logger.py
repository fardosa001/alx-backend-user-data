#!/usr/bin/env python3
"""Regex-ing"""
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = r'({})[^{}]+'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1{}'.format(redaction), message)