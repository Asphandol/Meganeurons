def josephus_survivor(n,k):
    people = [i for i in range(1, n+1)]
    k-=1
    index = k % len(people)
    
    while len(people)>1:
        people.pop(index)
        index = (index + k) % len(people)
    
    return people[0]
    
