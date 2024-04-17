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
    if not (isinstance(ch1, str) and len(ch1) == 1 and isinstance(ch2, str) and len(ch2) == 1):
        return

    res1 = ord(ch1.lower())
    res3 = ord(ch2.lower())

    return res1 > res3

if __name__=="__main__":
    import doctest
    print(doctest.testmod())