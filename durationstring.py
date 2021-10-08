"""
This module is unit-tested using doctest when run directly. :)
python duration_string.py
"""
import doctest
import re

TIMING_MAP = {"s": 1, "m": 60, "h": 60 * 60, "d": 24 * 60 * 60}


def get(string):
    """
    >>> get('2h')
    7200
    >>> get(' 2h ')
    7200
    >>> get(' 2 h ')
    7200
    >>> get('2s')
    2
    >>> get('1m')
    60
    >>> get('0.5m')
    30
    >>> get('2')
    2
    """
    if not string:
        if isinstance(string, int):
            string = str(int)
        else:
            raise ValueError("Invalid duration: %s" % string)

    string = re.sub(r"\s", "", string)
    value = re.sub(r"[^\d\.]", "", string)
    type_ = string.replace(value, "")
    multiplier = TIMING_MAP.get(type_, TIMING_MAP["s"])
    return int(multiplier * float(value))


if __name__ == "__main__":
    doctest.testmod()
