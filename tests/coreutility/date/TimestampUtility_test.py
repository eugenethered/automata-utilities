import unittest
from datetime import datetime

from coreutility.date.TimestampUtility import TimestampUtility


class TimestampUtilityTestCase(unittest.TestCase):

    def test_should_obtain_nanoseconds_time(self):
        nanoseconds = TimestampUtility.get_nanoseconds_time()
        self.assertEqual(len(str(nanoseconds)), 19)

    def test_should_obtain_utc_datetime_string(self):
        nanoseconds = 1662473484448608385
        datetime_string = TimestampUtility.to_datetime_string(nanoseconds)
        self.assertEqual(datetime_string, '2022-09-06T14:11:24.448608385Z')

    def test_should_obtain_datetime_from_nanoseconds(self):
        nanoseconds = 1662473484448608385
        actual_datetime = TimestampUtility.as_datetime_from_nanoseconds(nanoseconds)
        expected_datetime = datetime(2022, 9, 6, 14, 11, 24, 448608)
        self.assertEqual(actual_datetime, expected_datetime)

    def test_should_obtain_nanoseconds_from_datetime(self):
        # python cannot yet handle nano time (therefore-ish)
        nano_ish_datetime = datetime(2022, 9, 6, 14, 11, 24, 448608)
        nanoseconds = TimestampUtility.as_nanoseconds_from_datetime(nano_ish_datetime)
        self.assertEqual(nanoseconds, 1662473484448608)

    # todo: short nano-ish convert
    

if __name__ == '__main__':
    unittest.main()
