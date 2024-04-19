import random
import time
start_time = time.time()


def generate_grid() -> list[list[str]]:
    '''
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    '''
    lower_c = "BCDFGHJKLMNPQRSTVWXZ"
    lower_v = "AEIOU"
    gener_list = [[], [], []]

    for i in range(3):
        random_list = [random.choice(lower_c) for _ in range(2)] + [random.choice(lower_v)]
        gener_list[i] = random_list
    return gener_list

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    str, list[str] -> list[str]
    Reads the file f checks the words with rules, and returns a list of words.
    """
    if not isinstance(f, str) or not isinstance(letters, list):
        return []

    central_letter = letters[4]

    possible_words = []
    with open(f, "r", encoding="utf-8") as vocabulary:
        lines = vocabulary.read().splitlines()
        for line in lines:
            line = line.strip().lower()
            if 4 <= len(line) <= 9 and central_letter in line:
                for letter in line:
                    valid = True
                    if letter not in letters or letters.count(letter) < line.count(letter):
                        valid = False
                        break
                if valid and line not in possible_words:
                    possible_words.append(line)

    return possible_words





def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_list=[]
    while True:
        try:
            message = input().lower().strip()
            user_list.append(message)
        except EOFError:
            return user_list


def get_pure_user_words(user_words: list[str],
                        letters: list[str],
                        words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in the dictionary and are pure (may only contain the given central letter).
    """

    valid_words = [el for el in user_words if 4 <= len(el) <= 9 and \
    letters[4] in el and all(i in letters or el.count(i) == letters.count(i) for i in set(el))
    and el not in words_from_dict]
    return valid_words

def main():
    """
    Main function of target game
    """

    generate_letters = generate_grid()
    print("Your board is:")
    for sub_lst in generate_letters:
        print(sub_lst)

    print("\nPlease, suggest your words here:")
    becoming_lower = [letter.lower() for letters in generate_letters for letter in letters]
    user_list = get_user_words()
    valid_words = get_words("en.txt", becoming_lower)
    correct_words = [word for word in user_list if word in valid_words]
    incorrect_words = [word for word in user_list if word not in valid_words]

    print(f"Number of the right words: {len(correct_words)}")
    print("All possible words:")
    print(valid_words)
    print("\nYou missed the following words:")
    print(incorrect_words)
    pure_words = get_pure_user_words(user_list, becoming_lower, valid_words)

    print("\nYou suggest, but we don't have them in the dictionary:")
    print(pure_words)