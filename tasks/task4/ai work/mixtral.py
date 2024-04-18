import random
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
    # user_list=[]
    # while True:
    #     try:
    #         inp = input()
    #         x = inp.lower().strip()
    #         user_list.append(x)
    #     except EOFError:
    #         return user_list
    user_list=[]
    while True:
        try:
            user_list.extend(input().lower().strip().split())
        except EOFError:
            return user_list
