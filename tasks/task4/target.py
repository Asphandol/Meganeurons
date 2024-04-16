import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lower_c = "BCDFGHJKLMNPQRSTVWXZ"
    lower_v = "AEIOUY"
    random_list=[]
    ran_let=''
    gener_list =[[],[],[]]
    for k in range(6):
        ran_let = random.choice(lower_c)
        random_list.append(ran_let)
    for j in range(3):
        ran_let = random.choice(lower_v)
        random_list.append(ran_let)
    random.shuffle(random_list)
    k=3
    v=0
    for m in range(3):
        for i in range(v,k):
            gener_list[m].append(random_list[i])
        v+=3
        k+=3
    return gener_list


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    str, list[str] -> list[str]
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    possible_words = []
    if isinstance(f, str) and isinstance(letters, list):
        with open(f, "r", encoding ="utf-8") as vocabulary:
            for line in vocabulary:
                if 4<= len(line.strip())<=9 and letters[4] in line.strip().lower():
                    for el in line.strip():
                        res = 1
                        if el.lower() not in letters or \
line.lower().strip().count(el) > letters.count(el):
                            res = 0
                            break
                    if line.strip().lower() not in possible_words and res != 0:
                        possible_words.append(line.strip().lower())
                # if [a for a in line if a in letters and line.count(a)==letters.count(a)]:
                #     possible_words.append(line.strip().lower())
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
            inp = input()
            x = inp.lower().strip()
            user_list.append(x)
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
        if 4<= len(el)<=9 and letters[4] in el:
            for i in el:
                res = 1
                if i not in letters:
                    res = 0
                    break
            if el not in pure_words and res != 0 and el not in words_from_dict:
                pure_words.append(el)
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
