def get_middle(word):
    if not word:
        return ""

    middle_index = len(word) // 2
    if len(word) % 2 == 0:
        return word[middle_index - 1 : middle_index + 1]
    else:
        return word[middle_index]
    return "".join(char)
