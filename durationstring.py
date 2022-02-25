"""
This module is unit-tested using doctest when run directly. :)
python duration_string.py
"""
import doctest
import re

__version__ = "1.2.3"

TIMING_MAP = {"s": 1, "m": 60, "h": 60 * 60, "d": 24 * 60 * 60}


def is_valid(string):
    """
    >>> is_valid('')
    False
    >>> is_valid(None)
    False
    >>> is_valid('f')
    False
    >>> is_valid('2')
    True
    >>> is_valid('2x')
    False
    >>> is_valid('2s')
    True
    >>> is_valid(2)
    True
    >>> is_valid(' 2 ')
    True
    >>> is_valid(' 2h ')
    True
    >>> is_valid(' 2 h ')
    True
    """
    val, _ = is_valid_w_reason(string)
    return val


def is_valid_w_reason(string):
    if not string:
        return False, "Valid String value required."

    if not isinstance(string, str) and not isinstance(string, int):
        return False, "Invalid duration: %s" % string

    if isinstance(string, int):
        string = str(string)

    _, time_string = separate_time_string(string)
    if time_string and time_string not in TIMING_MAP:
        return (
            False,
            "Invalid duration string. Valid ones are %s"
            % ",".join(list(TIMING_MAP.keys())),
        )

    return True, ""


def separate_time_string(string):
    if isinstance(string, int):
        string = str(string)

    string = re.sub(r"\s", "", string)
    time_value = re.sub(r"[^\d\.]", "", string)
    time_string = string.replace(time_value, "")
    return time_value, time_string


def get_valid_time_parts(string):
    validity, reason = is_valid_w_reason(string)
    if not validity:
        raise ValueError(validity)

    return separate_time_string(string)


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
    >>> get(2)
    2
    """
    time_value, time_string = get_valid_time_parts(string)
    multiplier = TIMING_MAP.get(time_string, TIMING_MAP["s"])
    return int(multiplier * float(time_value))


if __name__ == "__main__":
    doctest.testmod()
