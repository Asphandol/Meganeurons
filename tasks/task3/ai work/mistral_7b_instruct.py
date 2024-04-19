'''Acronym'''
import re
import time
start_time = time.time()
def create_acronym(input_str: str) -> str | None:
    """
    >>> print(create_acronym("random access memory\\nAs soon As possible"))
    RAM - random access memory
    ASAP - As soon As possible
    >>> print(create_acronym("Hello my friend"))
    HMF - Hello my friend
    >>> print(create_acronym("12-3049"))
    None
    >>> create_acronym('random access memory\\n234')
    """

    if not input_str or not isinstance(input_str, str):
        return None

    sentences = re.split(r'\n+', input_str)
    acronyms = []
    for sentence in sentences:
        acr = ""
        for word in re.findall(r'\w+', sentence):
            if not word or not all(char.isalpha() for char in word):
                continue
            acr += word[0].upper()
        if not acr:
            return None
        acronyms.append(acr + " - " + sentence)
    return "\n".join(acronyms)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
