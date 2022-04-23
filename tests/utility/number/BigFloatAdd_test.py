import unittest

from core.number.BigFloat import BigFloat

from utility.number.BigFloatAdd import BigFloatAdd


class BigFloatAddTestCase(unittest.TestCase):

    def test_should_add_zeros(self):
        amount = BigFloat('0.00')
        other = BigFloat('0.00')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.00'))

    def test_should_add_number_based_big_floats(self):
        amount = BigFloat('1.00')
        other = BigFloat('1.00')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('2.00'))

    def test_should_add_fraction_based_big_floats(self):
        amount = BigFloat('0.01')
        other = BigFloat('0.01')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.02'))

    def test_should_add_large_fraction(self):
        amount = BigFloat('0.0100000001')
        other = BigFloat('0.0100000001')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.0200000002'))

    def test_should_add_fraction_which_needs_padding(self):
        amount = BigFloat('0.000000001')
        other = BigFloat('0.0000000001')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.0000000011'))

    def test_should_add_fraction_which_blows_to_next_fraction_unit(self):
        amount = BigFloat('0.0000000009')
        other = BigFloat('0.0000000009')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.0000000018'))

    def test_should_add_large_fraction_which_blows_to_next_fraction_unit(self):
        amount = BigFloat('0.0000000999')
        other = BigFloat('0.0000000009')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('0.0000001008'))

    def test_should_add_large_fraction_which_blows_to_next_number_unit(self):
        amount = BigFloat('0.9')
        other = BigFloat('0.9')
        result = BigFloatAdd(amount, other).result()
        self.assertEqual(result, BigFloat('1.8'))


if __name__ == '__main__':
    unittest.main()
