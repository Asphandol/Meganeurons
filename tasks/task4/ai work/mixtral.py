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
    random_list = [random.choice(lower_c) for _ in range(6)] 
    random_list += [random.choice(lower_v) for _ in range(3)]
    random.shuffle(random_list)
    return [random_list[i:i+3] for i in range(0, len(random_list), 3)]

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    str, list[str] -> list[str]
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    if not isinstance(f, str) or not isinstance(letters, list):
        return

    possible_words = []
    with open(f, "r", encoding ="utf-8") as vocabulary:
        for line in vocabulary:
            if 4<= len(line.strip())<=9 and letters[4] in line.strip().lower():
                for el in line.strip():
                    if (el.lower() not in letters or
                        line.lower().strip().count(el) > letters.count(el.lower())):
                        break
                else:
                    possible_words.append(line.strip().lower())
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
            user_list.extend(input().lower().strip().split())
        except EOFError:
            return user_list

def get_pure_user_words(user_words: list[str], \
letters: list[str], words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """

    pure_words=[]
    for el in user_words:
        if 4 <= len(el) <= 9 and letters[4] in el \
            and el not in pure_words \
            and all(i in letters for i in el) \
            and el not in words_from_dict:
            pure_words.append(el)
    return pure_words

def main():
    '''
    Main function of target game
    '''
    generate_letters = generate_grid()
    print(f"Your board is {generate_letters}")
    print("Please, suggest your words here:")
    lower_generate_letters = [k.lower() for el in generate_letters for k in el]
    counter = 0
    user_list = get_user_words()
    vocab_list = get_words("en.txt", lower_generate_letters )
    counter = sum(1 for el in user_list if el in vocab_list)
    print(f"Number of the right words: {counter}")
    print(f"All possible words:\n {vocab_list}\n")
    print(f"You missed the following words: \n {vocab_list.copy()}\n")
    print(f"You suggest, but we don`t have them in dictionary: \
{get_pure_user_words(user_list, lower_generate_letters, vocab_list)}")

end_time = time.time()

print("Execution Time: ", end_time - start_time)