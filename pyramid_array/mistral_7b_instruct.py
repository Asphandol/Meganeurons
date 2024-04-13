def pyramid(n):
    result = []
    index = 0

    while index <= n - 1:
        result.append([1] * (index + 1))
        index += 1

    return result