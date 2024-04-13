def pyramid(n):
    if n < 0:
        return ValueError("n should be non-negative")
    pyramid_list = []
    for i in range(1, n + 1):
        sub_list = [1] * i
        pyramid_list.append(sub_list)
    return pyramid_list
