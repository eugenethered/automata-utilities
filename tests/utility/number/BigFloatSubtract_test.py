import unittest

from core.number.BigFloat import BigFloat

from utility.number.BigFloatSubtract import BigFloatSubtract


class BigFloatSubtractTestCase(unittest.TestCase):

    def test_should_subtract_zeros(self):
        amount = BigFloat('0.00')
        other = BigFloat('0.00')
        result = BigFloatSubtract(amount, other).result()
        self.assertEqual(result, BigFloat('0.00'))

    def test_should_subtract_number_based_big_floats(self):
        amount = BigFloat('1.00')
        other = BigFloat('1.00')
        result = BigFloatSubtract(amount, other).result()
        self.assertEqual(result, BigFloat('0.00'))

    def test_should_subtract_and_sign_number_of_inverse_number_subtraction(self):
        amount = BigFloat('1.0')
        other = BigFloat('9.0')
        result = BigFloatSubtract(amount, other).result()
        self.assertEqual(result, BigFloat('-8.0'))


if __name__ == '__main__':
    unittest.main()
