"""Logs history of the stop watch"""
import os

log_file_name = "stop_watch_history.txt"


def append_to_log(data: str):
    """
    Append given data to log file
    :param data: given data
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        f = open(os.path.join(root_dir + os.sep + log_file_name), "a")  # open in append mode
        f.write(data)
        f.close()
    except FileNotFoundError:
        print("Error occurred, File not found")
    finally:
        print("Written to logs")
