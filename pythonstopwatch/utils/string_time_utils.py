"""String and Time utils for the project"""


def get_formatted_time(time):
    """
    Format the given time in nanoseconds into hours:minutes:seconds:milliseconds
    :param time: time in seconds
    :return: formatted time
    """
    assert time >= 0, "Value of time cannot be negative"
    hours = int(time / 10 ** 9 / 60 / 24)
    minutes = int(time / 10 ** 9 / 60)
    seconds = int(round(time / 10 ** 9 - minutes * 60.0, 2))
    milli_seconds = int(round((time / 10 ** 9 - minutes * 60.0 - seconds) * 100, 2))
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}:{milli_seconds:02d}'


def get_seconds_from_nanoseconds(nanoseconds) -> int:
    """
    Convert given nanoseconds to seconds
    :param nanoseconds: given time
    :return: seconds from nanoseconds
    """
    assert nanoseconds >= 0, "Value of time cannot be negative"
    return nanoseconds / 10 ** 9


def get_nanoseconds_from_seconds(seconds) -> int:
    """
    Convert given seconds to nanoseconds
    :param seconds: given time
    :return: nanoseconds to seconds
    """
    assert seconds >= 0, "Value of time cannot be negative"
    return seconds * 10 ** 9
