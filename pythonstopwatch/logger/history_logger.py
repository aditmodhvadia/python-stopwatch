"""Logs history of the stop watch"""
import os

LOG_FILE_NAME = "stop_watch_history.txt"


def append_to_log(data: str):
    """
    Append given data to log file
    :param data: given data
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        log_file = open(os.path.join(root_dir + os.sep + LOG_FILE_NAME), "a")  # open in append mode
        log_file.write(data)
        log_file.close()
    except FileNotFoundError:
        print("Error occurred, File not found")
    finally:
        print("Written to logs")
