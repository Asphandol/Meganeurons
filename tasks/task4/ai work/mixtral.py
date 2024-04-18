import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lower_c = "BCDFGHJKLMNPQRSTVWXZ"
    lower_v = "AEIOUY"
    random_list = [random.choice(lower_c) for _ in range(6)] 
    random_list += [random.choice(lower_v) for _ in range(3)]
    random.shuffle(random_list)
    return [random_list[i:i+3] for i in range(0, len(random_list), 3)]

print(generate_grid())