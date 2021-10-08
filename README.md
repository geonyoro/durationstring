# durationstring
A small module to assist in getting readable time in seconds that can be easily passed to time.sleep(*seconds*).

Converters
--------

- s - seconds
- m - minutes
- h - hours
- d - days

Failing to provide a converter will default to seconds.

Examples
--------
.. code-block:: python

    import duration_string
    import time

    time.sleep(duration_string.get("2m"))