import unittest
from unittest.mock import patch, mock_open

class TestCommonNames(unittest.TestCase):

    def test_common_names(self):
        female_names = ['Alice', 'Ava', 'Emma', 'Olivia', 'Sophia']
        male_names = ['Alexander', 'Andrew', 'Ethan', 'Isaac', 'Oliver']
        expected_output = {'Andrew', 'Ethan', 'Oliver'}
        self.assertEqual(common_names(female_names, male_names), expected_output)

    def test_common_names_empty_lists(self):
        female_names = []
        male_names = []
        expected_output = set()
        self.assertEqual(common_names(female_names, male_names), expected_output)

    def test_common_names_no_common_names(self):
        female_names = ['Alice', 'Ava', 'Emma', 'Olivia', 'Sophia']
        male_names = ['Jacob', 'Michael', 'William', 'Daniel', 'Matthew']
        expected_output = set()
        self.assertEqual(common_names(female_names, male_names), expected_output)

    def test_common_names_mixed_case(self):
        female_names = ['Alice', 'Ava', 'Emma', 'olivia', 'Sophia']
        male_names = ['Alexander', 'andrew', 'Ethan', 'Isaac', 'Oliver']
        expected_output = {'andrew', 'Ethan', 'Oliver'}
        self.assertEqual(common_names(female_names, male_names), expected_output)

    def test_common_names_non_alphabetic(self):
        female_names = ['Alice', 'Ava', 'Emma', 'Olivia', 'Sophia']
        male_names = ['Alexander', 'Andrew', 'Ethan123', 'Isaac', 'Oliver']
        expected_output = set()
        self.assertEqual(common_names(female_names, male_names), expected_output)

    def test_common_names_duplicate_names(self):
        female_names = ['Alice', 'Ava', 'Emma', 'Olivia', 'Olivia']
        male_names = ['Alexander', 'Andrew', 'Ethan', 'Isaac', 'Oliver', 'Oliver']
        expected_output = {'Andrew', 'Ethan', 'Oliver'}
        self.assertEqual(common_names(female_names, male_names), expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data='Alice\nEva\nOlivia')
    def test_names_read(self, mock_file):
        expected_output = ['Alice', 'Eva', 'Olivia']
        self.assertEqual(names_read('test.txt'), expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data='Alice\n\nEva\n\nOlivia\n')
    def test_names_read_with_empty_lines(self, mock_file):
        expected_output = ['Alice', 'Eva', 'Olivia']
        self.assertEqual(names_read('test.txt'), expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data='Alice\nEva\nolivia')
    def test_names_read_mixed_case(self, mock_file):
        expected_output = ['Alice', 'Eva', 'olivia']
        self.assertEqual(names_read('test_mixed.txt'), expected_output)

    def test_names_read_docstring(self):
        import doctest
        doctest.run_docstring_examples(names_read, globals(), name='names_read')

if __name__ == '__main__':
    unittest.main()