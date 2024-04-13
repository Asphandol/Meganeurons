def josephus_survivor(n, k):
    def josephus_perm(start, end):
        if start == end:
            return [start]
        index_to_remove = (start + k - 1) % (end - start) + start
        survivor = josephus_perm(index_to_remove + 1, end)
        return survivor + [end]
