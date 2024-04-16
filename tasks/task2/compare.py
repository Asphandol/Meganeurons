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
    if isinstance(ch1, str):
        if len(ch1) == 1:
            lower_alphabet="abcdefghijklmnopqrstuvwxyz"
            upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res1 = 0
            if ch1 in lower_alphabet:
                res1 += lower_alphabet.index(ch1) + 1
            elif ch1 in upper_alphabet:
                res1 += upper_alphabet.index(ch1) + 1
        else:
            return
    else:
        return
    if isinstance(ch2, str):
        if len(ch2) == 1:
            lower_alphabet="abcdefghijklmnopqrstuvwxyz"
            upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res3 = 0
            if ch2 in lower_alphabet:
                res3 += lower_alphabet.index(ch2) + 1
            elif ch2 in upper_alphabet:
                res3 += upper_alphabet.index(ch2) + 1
        else:
            return
    else:
        return
    return res1 > res3
