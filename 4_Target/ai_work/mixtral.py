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
print(get_words('4_Target/en.txt', [el for el in 'wumrovkif']))

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
        content = content[:-1]
        if (len(content) >= 4) and letters[4] in content:
            for letter in content:
                counter = 0
                if letter not in letters or content.count(letter) > letters.count(letter):
                    counter = 1
                    break
            if counter != 0:
                continue
            if content not in words_from_dict:
                full_list.append(content.lower())
    return full_list

# def main():
#     """
#     main function
#     """
    

