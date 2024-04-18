import time
import tracemalloc
import pandas as pd
import random

tracemalloc.start()
start_time = time.time()
'''
lab 11
Алгоритм, за яким прибульці забирають людей, нагадує
жадібний алгоритм. Ми вибираємо людей з найбільшим IQ та
забираємо їх. У цьому випадку це досить гарний підхід, але
він не завжди найоптимальніший.
'''

def read_file(file_path):
    '''
    Read the info from file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _=tmpfile.write('Elon Musk,165\\nMark Zuckerberg,152\\n\
Will Smith,157\\nMarilyn vos Savant,186\\nJudith Polgar,170')
    >>> print(read_file(tmpfile.name))
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
'Marilyn vos Savant': 186, 'Judith Polgar': 170}
    '''
    df = pd.read_csv(file_path, header=None, names=['Name', 'IQ'], engine='python')
    result = dict(df.to_numpy())

    return result

def selection_sort(lst):
    '''
    Selection sort algorithm
    to make lexical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j][0] < lst[min_idx][0] or (lst[j][0] == lst[min_idx][0] and lst[j][1] < lst[min_idx][1]):
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def quick_sort(arr):
    '''
    Quick sort algorithm
    to make lexical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''

    if len(arr) <= 1:
        return arr

    # Randomly choose the pivot
    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]
    arr.pop(pivot_index)

    low, high = [], []
    i = 0

    while i < len(arr) - 1: # notice the change, i should be less than the length minus one
        if i < len(arr) and arr[i][1] < pivot[1]:
            low.append(arr[i])
        elif i < len(arr) and arr[i][1] > pivot[1]:
            high.append(arr[i])
        i += 1

    return quick_sort(low) + arr[:i+1] + quick_sort(high)


def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    '''
    Counts the amount of travels to get people
    to another planet.

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
                      "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    all_trips = []
    taken = []

    iq_left = limit_iq

    while smarties:
        x = next((x for x in smarties if iq_left >= x[1]), (None, None))
        if x[0] is None:
            all_trips.append(taken[:])
            taken = []
            iq_left = limit_iq
            continue

        taken.append(x[0])
        smarties.remove(x)
        iq_left -= x[1]
    if taken:
        all_trips.append(taken[:])

    return len(all_trips) + (len(taken) == 0), all_trips


if __name__=='__main__':
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
