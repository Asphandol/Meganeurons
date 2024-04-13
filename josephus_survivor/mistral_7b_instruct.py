def josephus_survivor(n, k):
    if n == 1:
        return 1
    else:
        return (josephus_survivor(n - 1, k) + k) % n + 1
