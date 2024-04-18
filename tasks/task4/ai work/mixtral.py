import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lower_c = "BCDFGHJKLMNPQRSTVWXZ"
    lower_v = "AEIOUY"
    random_list=[]
    ran_let=''
    gener_list =[[],[],[]]
    random_list = [random.choice(lower_c) for k in range(6)]
    random_list += [random.choice(lower_v) for j in range(3)]
    random.shuffle(random_list)
    k=3
    v=0
    for m in range(3):
        for i in range(v,k):
            gener_list[m].append(random_list[i])
        v+=3
        k+=3
    return gener_list

print(generate_grid())