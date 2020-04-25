import time
import unittest

from pythonstopwatch.stopwatch import StopWatch
from pythonstopwatch.utils.string_time_utils import get_seconds_from_nanoseconds


class MyTestCase(unittest.TestCase):
    stop_watch: StopWatch

    def setUp(self) -> None:
        super().setUp()
        self.stop_watch = StopWatch(None)

    def test_stop_before_start(self):
        self.assertEqual(True, True)
        self.assertRaises(AssertionError, self.stop_watch.stop)

    def test_reset_before_start(self):
        self.assertEqual(True, True)
        self.assertRaises(AssertionError, self.stop_watch.reset)

    def test_reset_after_reset(self):
        self.assertEqual(True, True)
        self.stop_watch.start()
        self.stop_watch.reset()
        self.assertRaises(AssertionError, self.stop_watch.reset)

    def test_normal_flow(self):
        """
        Cannot stop before start
        Start
        Stop
        Reset
        Does not throw any error
        :return:
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


if __name__ == '__main__':
    unittest.main()
