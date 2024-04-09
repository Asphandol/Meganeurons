def snail(snail_map):
    snail_list = []
    while snail_map:
        snail_list.append(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]

    return [j for i in snail_list for j in i]
