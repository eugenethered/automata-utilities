import unittest

from utility.date_utility import generate_timestamp, format_to_utc_timestamp, as_file_timestamp


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


if __name__ == '__main__':
    unittest.main()
