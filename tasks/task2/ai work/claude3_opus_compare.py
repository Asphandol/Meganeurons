import time

start_time = time.time()

def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """
    if not (isinstance(ch1, str) and isinstance(ch2, str)):
        return None

    if len(ch1) != 1 or len(ch2) != 1:
        return None

    ch1 = ch1.lower()
    ch2 = ch2.lower()

    if not (ch1.isalpha() and ch2.isalpha()):
        return None

    return ord(ch1) > ord(ch2)

if __name__=="__main__":
    import doctest
    print(doctest.testmod())


end_time = time.time()

print("Execution Time: ", end_time - start_time)
