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
    random_list = random.choices(lower_c, k=6) + random.choices(lower_v, k=3)
    random.shuffle(random_list)
    return [random_list[i:i+3] for i in range(0, 9, 3)]

def get_words(f: str, letters: set[str]) -> set[str]:
    """
    str, set[str] -> set[str]
    Reads the file f. Checks the words with rules and returns a set of words.
    """
    possible_words = set()
    with open(f, "r", encoding="utf-8") as vocabulary:
        for line in vocabulary:
            word = line.strip().lower()
            if 4 <= len(word) <= 9 and letters[4] in word:
                if all(word.count(letter) <= letters.count(letter) for letter in word):
                    possible_words.add(word)
    return possible_words

def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_list = []
    while True:
        try:
            user_list.append(input().lower().strip())
        except EOFError:
            return user_list

def get_pure_user_words(user_words: list[str], letters: set[str], words_from_dict: set[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    for word in user_words:
        if 4 <= len(word) <= 9 and letters[4] in word:
            if all(letter in letters for letter in word) and word not in words_from_dict:
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