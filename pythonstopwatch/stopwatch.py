"""Stop Watch Frame"""
from time import time_ns
from tkinter import Frame, NONE, StringVar, Label, X, NO

from pythonstopwatch.utils.string_time_utils import get_formatted_time


def get_current_time():
    """
    Current time
    :return:
    """
    return time_ns()


class StopWatch(Frame):
    """
    StopWatch class
    """

    _is_running: bool = False  # Determine if the stopwatch is running or not

    _lap_times = []  # Hold lap times for the stopwatch

    _timer = None

    def __init__(self, parent=NONE, **kw):
        Frame.__init__(self, parent, kw)
        self._start_time = 0.0
        self._curr_time = 0.0
        self._end_time = 0.0
        self.time_str = StringVar()
        self.pack_time_label()

    def start(self):
        """
        Start the stop watch
        """
        if not self._is_running:
            # resume from where we left, or start from beginning
            self._start_time = get_current_time() - self._curr_time
            self._update_current_time()
            self._is_running = True

    def stop(self):
        """
        Stop the stopwatch
        """
        assert self._is_running, "Can't call stop if stopwatch is not running"
        if self._is_running:
            self.after_cancel(self._timer)
            self._curr_time = get_current_time() - self._start_time
            self._update_time(self._curr_time)
            self._end_time = get_current_time()
            self._is_running = False

    def reset(self):
        """
        Resets the stopwatch
        """
        assert self._start_time != self._end_time, "Can't call reset before start"
        self._is_running = True
        self.stop()
        self._start_time = get_current_time()
        self._curr_time = 0.0
        self._update_time(self._curr_time)

    def get_elapsed_time(self):
        """
        Get elapsed time for the stopwatch
        :return: current time - start time if running, end time - start time else
        """
        if self._is_running:
            elapsed_time = get_current_time() - self._start_time
        else:
            elapsed_time = self._end_time - self._start_time
        return elapsed_time

    def pack_time_label(self):
        """
        Create the time label for time and pack it
        """
        time_text = Label(self, textvariable=self.time_str, font=("times new roman", 60),
                          fg="white", bg="black", borderwidth=0, highlightthickness=0)
        self._update_time(self._curr_time)
        time_text.pack(fill=X, expand=NO, pady=45)

    def _update_time(self, elapsed_time):
        """
        Update the time to display
        :param elapsed_time: elapsed time in seconds
        """
        formatted_time = get_formatted_time(elapsed_time)
        self.time_str.set(formatted_time)

    def _update_current_time(self):
        """
        Update the current time and recurse after 50 milliseconds
        """
        self._curr_time = get_current_time() - self._start_time
        self._update_time(self._curr_time)
        # calls again after 50 milliseconds
        self._timer = self.after(50, self._update_current_time)

    def _set_running_state(self):
        """
        Set running state for the stopwatch
        """
        self._start_time = get_current_time()
        self._is_running = True

    def lap_time(self):
        """
        Record the lap time at the moment
        """
        assert self._is_running, "Cannot record lap time when stop watch is not running"

        self._lap_times.append(self.get_elapsed_time())

    def is_running(self):
        """
        :return: True, if stop watch is running else, False
        """
        return self._is_running

    def get_lap_times(self):
        """
        Get lap times
        :return: Lap Times
        """
        return self._lap_times

    def get_start_time(self):
        """
        Start time
        :return: Start time
        """
        return self._start_time

    def get_end_time(self):
        """
        End time
        :return: End time
        """
        return self._end_time


if __name__ == '__main__':
    pass
