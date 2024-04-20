import time
start_time = time.time()

''' Functions returns first letter of every word
'''

def create_acronym(sentence: str) -> str:
    """
    str -> str
    Creates acronym

    >>> print(create_acronym("random access memory\\nAs soon As possible"))
    RAM - random access memory
    ASAP - As soon As possible
    >>> print(create_acronym("Hello my friend"))
    HMF - Hello my friend
    >>> print(create_acronym("12-3049"))
    None
    >>> create_acronym('random access memory\\n234')
    """
    if not isinstance(sentence, str):
        return

    num_list = "0123456789"
    for char_index, char_value in enumerate(sentence):
        if char_value in num_list:
            return
    sentences = sentence.split("\n")
    acronyms = []
    for i, sentence in enumerate(sentences):
        words = sentence.split()
        acronym_word = "".join(word[0] for word in words)
        acronym_word = f"{acronym_word.upper()[0:3]} -"
        words.insert(0, acronym_word)
        if i < len(sentences) - 2:
            acronyms.extend(words + ["\n"])
        else:
            acronyms.extend(words)
    return " ".join(acronyms)


if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
