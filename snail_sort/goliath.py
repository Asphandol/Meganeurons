def snail(arr):
    result = []
    row, col = 0, 0
    is_clockwise = True

    for _ in range(2 * (len(arr) - 1) + 1):
        if is_clockwise:
            row += 1
            col -= 1
        else:
            row -= 1
            col += 1

        if row < 0 or row > len(arr) - 1 or col < 0 or col > len(arr[0]) - 1:
            is_clockwise = not is_clockwise
            continue

        result.append(arr[row][col])
        col += 2 if is_clockwise else -2

    return result
