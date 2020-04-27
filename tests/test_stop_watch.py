import time
import unittest
from tkinter import Tk

from pythonstopwatch.stopwatch import StopWatch
from pythonstopwatch.utils.string_time_utils import get_seconds_from_nanoseconds


class MyTestCase(unittest.TestCase):
    stop_watch: StopWatch

    def setUp(self) -> None:
        super().setUp()
        root = Tk()  # blank window
        self.stop_watch = StopWatch(root)

    def test_stop_before_start(self):
        """
        Should raise error when running stop before start
        :return:
        """
        self.assertRaises(AssertionError, self.stop_watch.stop)

    def test_reset_before_start(self):
        """
        Should raise error when running reset before start
        """
        self.assertRaises(AssertionError, self.stop_watch.reset)

    def test_reset_after_reset(self):
        """
        Should allow reset again after reset
        """
        self.stop_watch.start()
        self.stop_watch.reset()
        self.stop_watch.reset()

    def test_normal_flow(self):
        """
        Elapsed time should almost match the expected time
        """
        elapsed_time_expected = .200
        self.test_stop_before_start()
        self.stop_watch.start()
        time.sleep(elapsed_time_expected)
        self.stop_watch.stop()
        self.assertAlmostEqual(
            get_seconds_from_nanoseconds(self.stop_watch.get_elapsed_time()),
            elapsed_time_expected, places=2)  # replace with elapsed time
        self.stop_watch.reset()

    def test_lap_times_recorded_correctly(self):
        """
        Recording 3 laps should reflect 3 lap times stored
        """
        self.stop_watch.start()
        time.sleep(.05)
        self.stop_watch.lap_time()
        time.sleep(.05)
        self.stop_watch.lap_time()
        time.sleep(.05)
        self.stop_watch.lap_time()
        self.stop_watch.stop()
        self.assertEqual(3, len(self.stop_watch.get_lap_times()))

        pass


if __name__ == '__main__':
    unittest.main()
