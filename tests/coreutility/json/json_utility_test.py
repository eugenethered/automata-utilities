import unittest

from coreutility.collection.dictionary_utility import as_data
from coreutility.json.json_utility import as_json, as_pretty_json


class JsonUtilityTestCase(unittest.TestCase):

    def test_should_load_json_data(self):
        json_string = '{"instrument": "CASH","ignore": true}'
        json_data = as_json(json_string)
        self.assertEqual('CASH', json_data['instrument'])
        self.assertEqual(True, json_data['ignore'])

    def test_should_obtain_json_to_data(self):
        json_string = '{"instrument": "CASH","ignore": true}'
        json_data = as_json(json_string)
        self.assertEqual('CASH', as_data(json_data, 'instrument'))
        self.assertEqual(True, as_data(json_data, 'ignore'))

    def test_should_obtain_no_json_to_data_when_data_in_json_does_not_exist(self):
        json_string = '{"instrument": "CASH","ignore": true}'
        json_data = as_json(json_string)
        self.assertEqual(None, as_data(json_data, 'SomethingNotThere'))

    def test_should_obtain_default_data_when_data_in_json_does_not_exist(self):
        json_string = '{"instrument": "CASH"}'
        json_data = as_json(json_string)
        self.assertEqual(None, as_data(json_data, 'SomethingNotThere'), 'Should use default None')
        self.assertEqual(False, as_data(json_data, 'SomethingNotThere', default=False), 'Should override default from None to False')
        self.assertEqual(True, as_data(json_data, 'SomethingNotThere', default=True), 'Should override default from None to True')

    def test_override_json_default_when_data_is_empty(self):
        json_data = as_json('', '{}')
        self.assertEqual({}, json_data)

    def test_return_json_default_when_data_is_empty(self):
        json_data = as_json('')
        self.assertEqual([], json_data)

    def test_return_json_default_when_data_is_none(self):
        json_data = as_json(None)
        self.assertEqual([], json_data)

    def test_should_serialize_json_to_default_4_indent_string(self):
        json_string = '{"instrument": "CASH", "ignore": true}'
        json_data = as_json(json_string)
        serialized = as_pretty_json(json_data)
        expected = '{\n' \
                   '    "ignore": true,\n' \
                   '    "instrument": "CASH"\n' \
                   '}'
        self.assertEqual(expected, serialized)

    def test_should_serialize_json_to_no_indented_string(self):
        json_string = '{"instrument": "CASH", "ignore": true}'
        json_data = as_json(json_string)
        serialized = as_pretty_json(json_data, indent=None)
        expected = '{"ignore": true, "instrument": "CASH"}'
        self.assertEqual(expected, serialized)


if __name__ == '__main__':
    unittest.main()
