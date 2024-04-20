import random
import time
start_time = time.time()

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lower_c = "BCDFGHJKLMNPQRSTVWXZ"
    lower_v = "AEIOUY"
    grid = [[], [], []]


    for _ in range(3):
        grid.append([])
        for _ in range(3):
            if random.randint(0, 1) == 0:
                letter = random.choice(lower_v)
            else:
                letter = random.choice(lower_c)
            grid[-1].append(letter)

    return grid


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    str, list[str] -> list[str]
    Reads the letter_counts file. Checks the words with rules and returns a list of words.
    """
    possible_words = []
    if isinstance(f, str) and isinstance(letters, list):
        with open(f, "r", encoding="utf-8") as vocabulary:
            for line in vocabulary:
                word = line.strip().lower()
                if 4 <= len(word) <= 9 and letters[4] in word:
                    letter_counts = {}
                    for char_ in word:
                        letter_counts[char_] = letter_counts.get(char_, 0) + 1
                    for char_count in letter_counts.values():
                        if char_count > letters.count(char_):
                            break
                    else:
                        if word not in possible_words:
                            possible_words.append(word)
    return possible_words


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d for *nix or Ctrl-Z+Enter for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_list = []
    while True:
        try:
            inp = input().lower().strip()
            if inp:
                user_list.append(inp)
        except EOFError:
            return user_list
        

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns a list of those words
    that are not in the dictionary.
    """
    pure_words = []
    for word in user_words:
        if 4 <= len(word) <= 9 and letters[4] in word:
            for char_ in word:
                if char_ not in letters:
                    break
                else:
                    if word not in pure_words and word not in words_from_dict:
                        pure_words.append(word)
    return pure_words


def main():
    '''
    Main function of target game
    '''
    generate_letters = generate_grid()
    print(f"Your board is {generate_letters}")
    print("Please, suggest your words here:")
    lower_generate_letters =[]
    for el in generate_letters:
        for k in el:
            lower_generate_letters.append(k.lower())
    counter = 0
    user_list = get_user_words()
    vocab_list = get_words("en.txt", lower_generate_letters )
    for el in user_list:
        if el in vocab_list.copy():
            counter +=1
            del el
    print(f"Number of the right words: {counter}")
    print(f"All possible words:\n {vocab_list}\n")
    print(f"You missed the following words: \n {vocab_list.copy()}\n")
    print(f"You suggest, but we don`t have them in dictionary: \
{get_pure_user_words(user_list, lower_generate_letters, vocab_list)}")
end_time = time.time()

print("Execution Time: ", end_time - start_time)
