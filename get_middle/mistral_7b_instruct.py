def get_middle(s):
    middle = ''
    length = len(s)

    if length % 2 == 0:
        index = length // 2
        middle = s[index - 1] + s[index]
    else:
        index = length // 2
        middle = s[index]

    return middle