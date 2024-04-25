import unittest
import random
from target_game import *

class TestGenerateGrid(unittest.TestCase):

    def setUp(self) -> None:
        self.letters1 = ['a', 'e', 'i', 'o', 'p', 'r', 's', 't', 'u']

    def test_generate_grid_returns_list_of_three_sublists(self):
        # Arrange

        # Act
        grid = generate_grid()

        # Assert
        self.assertEqual(len(grid), 3)

    def test_each_sublist_has_exactly_three_elements(self):
        # Arrange

        # Act
        grid = generate_grid()

        # Assert
        for sublist in grid:
            self.assertEqual(len(sublist), 3)

    def test_each_sublist_contains_at_least_one_vowel(self):
        # Arrange

        # Act
        grid = generate_grid()

        # Assert
        for sublist in grid:
            self.assertGreater(len([x for x in sublist if x in ['A', 'E', 'I', 'O', 'U']]), 0)

    def test_grid_contains_only_letters(self):
        # Arrange

        # Act
        grid = generate_grid()

        # Assert
        for sublist in grid:
            self.assertIsInstance(sublist, list)
            self.assertTrue(all(isinstance(x, str) for x in sublist))


    def test_get_pure_user_words(self):
        user_words = ['apple', 'banana', 'pear', 'grape', 'appear']
        words_from_dict = ['apple', 'banana', 'pear', 'orange']

        result = get_pure_user_words(user_words, self.letters1, words_from_dict)
        self.assertEqual(result, ['appear'])

    def test_get_words(self):
        f = "words.txt"
        letters = ['a', 'e', 'i', 'o', 'p', 'r', 's', 'l', 'p']

        result = get_words(f, letters)

        self.assertEqual(result, ['apples'])




# if __name__ == '__main__':
#     unittest.main()
