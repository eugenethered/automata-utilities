import unittest
from datetime import datetime

from coreutility.date.NanoTimestamp import NanoTimestamp


class NanoTimestampTestCase(unittest.TestCase):

    def test_should_obtain_nanoseconds_time(self):
        nanoseconds = NanoTimestamp.get_nanoseconds()
        self.assertEqual(len(str(nanoseconds)), 19)

    def test_should_obtain_datetime_from_nanoseconds(self):
        nanoseconds = 1662473484448608385
        actual_datetime = NanoTimestamp.as_datetime(nanoseconds)
        expected_datetime = datetime(2022, 9, 6, 14, 11, 24, 448608)
        self.assertEqual(actual_datetime, expected_datetime)

    def test_should_obtain_nanoseconds_from_datetime(self):
        # python cannot yet handle nano time (therefore-ish)
        nano_ish_datetime = datetime(2022, 9, 6, 14, 11, 24, 448608)
        nanoseconds = NanoTimestamp.as_nanoseconds(nano_ish_datetime)
        self.assertEqual(nanoseconds, 1662473484448608)

    def test_should_obtain_utc_datetime_string_from_nanoseconds(self):
        nanoseconds = 1662473484448608385
        datetime_string = NanoTimestamp.to_string(nanoseconds)
        self.assertEqual(datetime_string, '2022-09-06T14:11:24.448608385Z')

    def test_should_obtain_utc_datetime_string_from_short_nano_ish_seconds(self):
        nanoseconds = 1662473484448608
        datetime_string = NanoTimestamp.to_string(nanoseconds)
        self.assertEqual(datetime_string, '2022-09-06T14:11:24.448608Z')

    def test_should_obtain_utc_datetime_string_from_datetime(self):
        nano_ish_datetime = datetime(2022, 9, 6, 14, 11, 24, 448608)
        datetime_string = NanoTimestamp.to_string(nano_ish_datetime)
        self.assertEqual(datetime_string, '2022-09-06T14:11:24.448608Z')


if __name__ == '__main__':
    unittest.main()
