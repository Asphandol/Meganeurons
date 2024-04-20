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
    if not (isinstance(ch1, str) and isinstance(ch2, str) and len(ch1) == 1 and len(ch2) == 1):
        return

    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def char_index(char_):
        return (lower_alphabet.index(char_) if char_.islower() 
                else upper_alphabet.index(char_.upper()))

    res1 = char_index(ch1) + 1 if ch1.isalpha() else 0
    res2 = char_index(ch2) + 1 if ch2.isalpha() else 0

    return res1 > res2

if __name__=="__main__":
    import doctest
    print(doctest.testmod())


end_time = time.time()

print("Execution Time: ", end_time - start_time)
