import unittest
import random
from string import ascii_lowercase

class TestSolution(unittest.TestCase):
    def test_generate_grid(self):
        # Test that the function returns a list of lists
        grid = generate_grid()
        self.assertIsInstance(grid, list)
        self.assertIsInstance(grid[0], list)

        # Test that the grid has 9 letters
        self.assertEqual(len(grid), 3)
        self.assertEqual(len(grid[0]), 3)
        self.assertEqual(len(grid[1]), 3)
        self.assertEqual(len(grid[2]), 3)

        # Test that the letters are strings
        for row in grid:
            for letter in row:
                self.assertIsInstance(letter, str)

        # Test that the grid has the correct number of vowels and consonants
        vowels = 'aeiou'
        vowel_count = 0
        consonant_count = 0
        for row in grid:
            for letter in row:
                if letter.lower() in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        self.assertEqual(vowel_count, 3)
        self.assertEqual(consonant_count, 6)

    def test_get_user_words(self):
        # Test with a sample input
        user_input = ['upper', 'pet', 'uproot', 'open', 'opto', '']
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            words = get_user_words()
        self.assertEqual(words, ['upper', 'pet', 'uproot', 'open', 'opto'])

    def test_get_words(self):
        # Test with a sample grid and dictionary
        grid = [['E', 'T', 'O'], ['O', 'P', 'N'], ['P', 'U', 'R']]
        letters = [letter for row in grid for letter in row]
        with open('en.txt', 'r') as f:
            dictionary = f.read().splitlines()
        words = get_words('en.txt', letters)

        # Test that all words are in the dictionary
        for word in words:
            self.assertIn(word, dictionary)

        # Test that all words are at least 4 letters long
        for word in words:
            self.assertGreaterEqual(len(word), 4)

        # Test that all words contain a central letter
        central_letters = ['o', 'p', 'n']
        for word in words:
            self.assertTrue(any(letter in word for letter in central_letters))

        # Test that there are no duplicates
        self.assertEqual(len(words), len(set(words)))

    def test_get_pure_user_words(self):
        user_words = ['upper', 'pet', 'uproot', 'open', 'opto']
        grid = [['E', 'T', 'O'], ['O', 'P', 'N'], ['P', 'U', 'R']]
        letters = [letter for row in grid for letter in row]
        with open('en.txt', 'r') as f:
            dictionary = f.read().splitlines()
        words_from_dict = get_words('en.txt', letters)
        pure_user_words = get_pure_user_words(user_words, letters, words_from_dict)

        # Test that all pure_user_words are in user_words
        for word in pure_user_words:
            self.assertIn(word, user_words)

        # Test that all pure_user_words are not in words_from_dict
        for word in pure_user_words:
            self.assertNotIn(word, words_from_dict)

        # Test that all pure_user_words are at least 4 letters long
        for word in pure_user_words:
            self.assertGreaterEqual(len(word), 4)

        # Test that all pure_user_words contain a central letter
        central_letters = ['o', 'p', 'n']
        for word in pure_user_words:
            self.assertTrue(any(letter in word for letter in central_letters))

        # Test that all pure_user_words are made up of letters from the grid
        for word in pure_user_words:
            for letter in word:
                self.assertIn(letter, letters)

    def test_generate_grid_edge_cases(self):
        # Test that the grid is not empty
        with self.assertRaises(ValueError):
            generate_grid(0)

        # Test that the grid size is valid
        with self.assertRaises(ValueError):
            generate_grid(-1)
        with self.assertRaises(ValueError):
            generate_grid(4)

    def test_get_user_words_edge_cases(self):
        # Test with empty input
        user_input = ['']
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            words = get_user_words()
        self.assertEqual(words, [])

        # Test with non-string input
        user_input = ['123', '']
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            words = get_user_words()
        self.assertEqual(words, [])

    def test_get_words_edge_cases(self):
        # Test with an empty grid
        grid = []
        letters = []
        words = get_words('en.txt', letters)
        self.assertEqual(words, [])

        # Test with a grid containing non-alphabetic characters
        grid = [['@', '#', '$'], ['%', '^', '&'], ['*', '(', ')']]
        letters = [letter for row in grid for letter in row]
        words = get_words('en.txt', letters)
        self.assertEqual(words, [])

    def test_get_pure_user_words_edge_cases(self):
        # Test with an empty user_words list
        user_words = []
        grid = [['E', 'T', 'O'], ['O', 'P', 'N'], ['P', 'U', 'R']]
        letters = [letter for row in grid for letter in row]
        with open('en.txt', 'r') as f:
            dictionary = f.read().splitlines()
        words_from_dict = get_words('en.txt', letters)
        pure_user_words = get_pure_user_words(user_words, letters, words_from_dict)
        self.assertEqual(pure_user_words, [])

        # Test with user_words containing non-alphabetic characters
        user_words = ['up@er', 'p3t', 'upr00t', 'op3n', 'opto']
        pure_user_words = get_pure_user_words(user_words, letters, words_from_dict)
        self.assertEqual(pure_user_words, [])

if __name__ == '__main__':
    unittest.main()
