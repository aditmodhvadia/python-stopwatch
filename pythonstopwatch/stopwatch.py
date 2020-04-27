"""Stop Watch Frame"""
from time import time_ns
from tkinter import Frame, NONE, StringVar, Label, X, NO, RIGHT
from typing import List

from pythonstopwatch.logger.history_logger import append_to_log
from pythonstopwatch.utils.string_time_utils import get_formatted_time


def get_current_time():
    """
    Current time
    :return:
    """
    return time_ns()


class LapTime:
    """
    LapTime Class
    """

    def __init__(self, lap_time: float, split_time: float):
        """__init__"""
        self.lap_time = lap_time
        self.split_time = split_time


def get_formatted_lap_str(lap, position):
    """
    Get the Lap Time for the given lap in the format
    :param lap: given lap
    :param position: position of lap
    :return: Formatted lap
    """
    return f'{position}  {get_formatted_time(lap.lap_time)}' \
           f'\n    {get_formatted_time(lap.split_time)}\n\n'


class StopWatch(Frame):
    """
    StopWatch class
    """

    _is_running: bool = False  # Determine if the stopwatch is running or not

    _lap_times: List[LapTime] = []  # Hold lap times for the stopwatch

    _timer = None

    def __init__(self, parent=NONE, **kw):
        Frame.__init__(self, parent, kw)
        self._start_time = 0.0
        self._curr_time = 0.0
        self._end_time = 0.0
        self._lap_times = []
        self.time_str = StringVar()
        self.lap_str = StringVar()
        time_text = Label(self, textvariable=self.time_str, font=("times new roman", 60),
                          fg="white", bg="black", borderwidth=0, highlightthickness=0)
        self._update_time(self._curr_time)
        time_text.pack(pady=35)
        lap_text = Label(self, textvariable=self.lap_str, font=("times new roman", 10),
                         fg="white", bg="black", borderwidth=0, highlightthickness=0)
        lap_text.pack(side=RIGHT, fill=X, expand=NO)
        self._update_lap_time()

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
        append_to_log(self.__repr__())
        self._start_time = get_current_time()
        self._curr_time = 0.0
        self._update_time(self._curr_time)
        self._lap_times = []
        self._update_lap_time()

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
        if len(self._lap_times) == 0:
            split_time = self.get_elapsed_time()
        else:
            split_time = self.get_elapsed_time() - self._lap_times[-1].lap_time
        self._lap_times.append(LapTime(self.get_elapsed_time(), split_time))
        self._update_lap_time()

    def _update_lap_time(self):
        """
        Update the lap time to display
        """
        formatted_lap_time = self.get_formatted_lap_time()
        self.lap_str.set(formatted_lap_time)

    def get_formatted_lap_time(self):
        """
        Get all lap times in formatted form
        :return: Formatted Lap Times
        """
        formatted_lap_str = ''
        if len(self._lap_times) != 0:
            formatted_lap_str = f'Laps\nSplits\n\n'
            len_lap_time = len(self._lap_times)
            for index in range(len_lap_time):
                # display from the back with position starting with 1
                formatted_lap_str += \
                    get_formatted_lap_str(self._lap_times[-1 - index], len_lap_time - index)
        return formatted_lap_str

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

    def __repr__(self):
        """
        Represent the object in a formatted way showing it's attributes
        :return: Formatted object with it's attributes
        """
        laps = "Lap/Split times\n"
        for index in range(len(self._lap_times)):
            position = len(self._lap_times) - index
            laps += get_formatted_lap_str(self._lap_times[-1 - index], position)
        return f'Stop watch: End Time:{get_formatted_time(self._end_time - self._start_time)} ' \
               f'\n{laps}'

    if __name__ == '__main__':
        pass
