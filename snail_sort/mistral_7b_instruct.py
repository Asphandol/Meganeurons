def snail_map(snail_map):
    outer_edge = []

    for i in range(len(snail_map)):
        # First step: Traverse each row till middle (n/2 -1)
        for j in range(len(snail_map[0])):
            outer_edge.append(snail_map[i][j] + outer_edge.pop() if i < len(snail_map) - 1 else outer_edge.append(snail_map[i][j])
        snail_map[i].pop(0)

    middle = outer_edge.pop() # last item in outer_edge (middle value)

    snail_map += outer_edge[::-1] # reversing diagonal elements
    snail_map[0].append(middle)
    # Final diagonal
    return snail_map[::len(snail_map) // 2][::len(snail_map) - 1][:len(snail_map)//2][:]