def snail(array):
    snail_array = []
    while array:
        snail_array += array.pop(0)
        array = list(zip(*array))[::-1]
    return snail_array