import time

start_time = time.time()

def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two chars by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    """
    if not (isinstance(ch1, str) and isinstance(ch2, str)):
        return None

    return ch1.lower() > ch2.lower()

if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print(f"Execution Time: {end_time - start_time}")
