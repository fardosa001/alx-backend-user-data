#!/usr/bin/env python3
"""Regex-ing"""
import logging
import csv
import os
import re
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "credit_card")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format method to filter values in incoming log records."""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Return a logging.Logger object configured as requested."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    formatter = RedactingFormatter(PII_FIELDS)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger
