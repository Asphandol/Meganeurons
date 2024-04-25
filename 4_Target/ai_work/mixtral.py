'''
ababalamaga
'''
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    a_alphabet = ['A', 'E', 'I', 'O', 'U', 'Y']
    b_alphabet = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', \
'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    a_num = random.sample(a_alphabet, 3)
    b_num = random.sample(b_alphabet, 6)
    full_list = a_num + b_num
    random.shuffle(full_list)
    full_list = [full_list[0:3], full_list[3:6], full_list[6:]]
    return full_list

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """

    full_list = []
    randoze = letters

    with open(f, 'r', encoding='UTF-8') as file_:
        for content in file_:
            content = content.strip().lower()
            if (len(content) >= 4) and randoze[4] in content:
                for letter in content:
                    counter = 0
                    if letter not in randoze or content.count(letter) > randoze.count(letter):
                        counter = 1
                        break
                if counter != 0:
                    continue
                full_list.append(content.lower())

        return full_list


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    full_list = []
    while 1:
        try:
            a = input()
            full_list.append(a)
        except EOFError:
            break
    return full_list

def get_pure_user_words(user_words: list[str], letters: list[str], \
words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    full_list = []
    for content in user_words:
        # Convert content to lowercase and strip '\n'
        content = content.strip().lower()
        if 4 <= len(content) <= 9 and letters[4] in content and all(x in letters for x in content):
            if content not in words_from_dict:
                full_list.append(content)
    return full_list

def main():
    """
    main function
    """
    pass

import unittest

class TestGeneratrGrid(unittest.TestCase):
    def test_generate_grid(self):
        result = generate_grid()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        for sublist in result:
            self.assertIsInstance(sublist, list)
            self.assertEqual(len(sublist), 3)
            for item in sublist:
                self.assertIsInstance(item, str)
                self.assertTrue(len(item) == 1)
                self.assertRegex(item, r'[A-Z]')

class TestGetWords(unittest.TestCase):
    def setUp(self):
        self.letters = ['A', 'E', 'J', 'B', 'C', 'H']
        self.content = 'ababalamaga'

    def test_get_words(self):
        result = get_words('4_Target/en.txt', self.letters)
        self.assertIsInstance(result, list)
        for word in result:
            self.assertIsInstance(word, str)
            self.assertTrue(len(word) >= 4)
            self.assertRegex(word, r'\b[aejbh]*[AEJBH][aejbh]*\b')

    def test_get_words_empty(self):
        result = get_words('4_Target/en.txt', self.letters)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
