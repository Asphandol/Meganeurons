import time

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
        return None

    lines = sentence.split("\n")
    result = []

    for line in lines:
        if any(char.isdigit() for char in line):
            return None

        words = line.split()
        acronym = "".join(word[0].upper() for word in words)
        result.append(f"{acronym} - {line}")

    return "\n".join(result)

start_time = time.time()
print(create_acronym("random access memory\nAs soon As possible"))
end_time = time.time()
print("Execution Time: ", end_time - start_time)
