def get_middle(word):
    length = len(word)
    if length % 2 == 1:
        return word[length // 2]
    else:
        middle_index_1 = length // 2 - 1
        middle_index_2 = length // 2
        return word[middle_index_1:middle_index_2 + 1]
