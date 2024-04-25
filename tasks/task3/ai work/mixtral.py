import time
start_time = time.time()


def create_acronym(input_sentence: str) -> str:
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
    if isinstance(input_sentence, str):
        if any(char.isdigit() for char in input_sentence):
            return

        sentences = input_sentence.split("\n")

        acronyms = []

        for i, sentence in enumerate(sentences):
            if sentence.isdigit():
                continue
        
            words = sentence.split()
        
            acronym = "".join(word[0].upper() for word in words)
        
            words = [acronym] + [' '.join(words)]
        
            words = " - ".join(words)
        
            if i < len(sentences) - 1:
                acronyms.append(words)
                acronyms.append("\n")
            else:
                acronyms.append(words)
        
        acronyms = "".join(acronyms)

        return acronyms
    
if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)