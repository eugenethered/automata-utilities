import unittest

from utility.string_utility import is_empty


class StringUtilityTestCase(unittest.TestCase):

    def test_should_result_in_empty_none_string(self):
        self.assertTrue(is_empty(None))

    def test_should_result_in_empty_string(self):
        self.assertTrue(is_empty(''))

    def test_should_result_in_empty_blank_string(self):
        self.assertTrue(is_empty('    '))

    def test_should_not_be_empty_string(self):
        self.assertFalse(is_empty('the cat in the hat'))
        self.assertFalse(is_empty('   dog    '))


if __name__ == '__main__':
    unittest.main()
