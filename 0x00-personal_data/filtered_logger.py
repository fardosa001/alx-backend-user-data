#!/usr/bin/env python3
"""Regex-ing"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    return re.sub(r'({})[^{}]+'.format('|'.join(fields), separator),
                  r'\1{}'.format(redaction), message)
