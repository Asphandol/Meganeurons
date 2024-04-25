import unittest
from common_names import *

class TestCommonNames(unittest.TestCase):

    def setUp(self) -> None:
        self.female_names = names_read('female_names.txt')
        self.male_names = names_read('male_names.txt')

    def test_common_names(self):
        expected_result = {"Alex", "Ava"}
        result = common_names(self.female_names, self.male_names)
        self.assertSetEqual(expected_result, result)

    def test_empty_male_names(self):
        self.assertEqual(set(), common_names( [], self.female_names ))

    def test_empty_female_names(self):
        self.assertEqual(set(), common_names( self.male_names, [] ))

    def test_single_name_male(self):
        self.assertEqual(set(), common_names(['Alice'], self.female_names))

    def test_single_name_female(self):
        self.assertEqual(set(), common_names(self.male_names, ['Alice']))

    def test_common_names_generic_case(self):
        self.assertSetEqual(set(['Alex', 'Ava']), common_names(['Alex', 'Ava'], ['Alex', 'Ava']))

    def test_common_names_duplicates(self):
        self.assertEqual(set(['Alex', 'Ava']), common_names(self.male_names + ['Alex'], self.female_names + ['Ava']))


    # Replace Test cases for empty, none, has_different_lengths, and non_file as they are already covered by the setUp

# if __name__ == '__main__':
#     unittest.main()
