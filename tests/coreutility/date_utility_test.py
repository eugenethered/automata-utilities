import unittest
from time import sleep

from coreutility.date_utility import generate_timestamp, format_to_utc_timestamp, as_file_timestamp, get_utc_timestamp, as_nano_second_timestamp


class DateUtilityTestCase(unittest.TestCase):

    def test_generates_UTC_timestamp(self):
        timestamp = generate_timestamp()
        self.assertRegex(timestamp.__str__(), r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\+00:00$')

    def test_should_obtain_timestamp_from_utc_string(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516+00:00')
        self.assertEqual('2021-12-22 15:36:05.565516+00:00', timestamp.__str__())

    def test_format_timestamp_for_files(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516+00:00')
        file_timestamp = as_file_timestamp(timestamp)
        self.assertEqual('20211222_153605_565516', file_timestamp)

    def test_should_get_utc_timestamp(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516+00:00')
        utc_timestamp = get_utc_timestamp(timestamp)
        self.assertEqual(1640187365565, utc_timestamp)

    def test_should_get_different_utc_timestamps(self):
        utc_timestamp = get_utc_timestamp()
        sleep(0.100)
        another_utc_timestamp = get_utc_timestamp()
        self.assertNotEqual(utc_timestamp, another_utc_timestamp)
        self.assertTrue(another_utc_timestamp > utc_timestamp)

    def test_should_obtain_time_in_nano_second_format(self):
        timestamp = as_nano_second_timestamp()
        self.assertRegex(timestamp.__str__(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$')

    def test_should_generate_nano_time_from_formatted_time(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516+00:00')
        nano_timestamp = as_nano_second_timestamp(timestamp)
        self.assertEqual(nano_timestamp, '2021-12-22T15:36:05.565Z')

    def test_should_generate_shortened_nano_time_from_formatted_time_with_z(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516')
        nano_timestamp = as_nano_second_timestamp(timestamp)
        self.assertEqual(nano_timestamp, '2021-12-22T15:36:05.565Z')

    def test_should_generate_nano_time_from_formatted_time_with_z(self):
        timestamp = format_to_utc_timestamp('2021-12-22T15:36:05.565516')
        nano_timestamp = as_nano_second_timestamp(timestamp)
        self.assertEqual(nano_timestamp, '2021-12-22T15:36:05.565Z')


if __name__ == '__main__':
    unittest.main()
