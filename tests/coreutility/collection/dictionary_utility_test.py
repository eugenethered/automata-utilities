import unittest

from coreutility.collection.dictionary_utility import as_data


class DictionaryUtilityTestCase(unittest.TestCase):

    def test_should_load_obtain_data(self):
        dictionary = {'instrument': 'CASH', 'ignore': True}
        self.assertEqual('CASH', as_data(dictionary, 'instrument'))
        self.assertEqual(True, as_data(dictionary, 'ignore'))


if __name__ == '__main__':
    unittest.main()
