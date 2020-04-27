import unittest
from pythonstopwatch.utils.string_time_utils import get_formatted_time, get_seconds_from_nanoseconds, \
    get_nanoseconds_from_seconds


class BasicTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_negative_time_value(self):
        value = -123
        self.assertRaises(AssertionError, lambda: get_formatted_time(value))

    def test_format_time_to_string_2_min_85_millis(self):
        value = get_nanoseconds_from_seconds(2 * 60 + 0.85)  # 2 mins and 85 milliseconds
        expected = "00:02:00.85"
        self.assertEqual(expected, get_formatted_time(value))

    def test_format_time_to_string_2587_seconds(self):
        value = get_nanoseconds_from_seconds(2587.63)
        expected = "01:43:07.63"
        self.assertEqual(expected, get_formatted_time(value))

    def test_format_time_to_string_1_min_101_millis(self):
        value = get_nanoseconds_from_seconds(60.101)
        expected = "00:01:00.10"
        self.assertEqual(expected, get_formatted_time(value))

    def test_nano_to_seconds_negative_value(self):
        value = -100
        self.assertRaises(AssertionError, lambda: get_seconds_from_nanoseconds(value))


if __name__ == '__main__':
    unittest.main()
