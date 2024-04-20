import time
import tracemalloc

tracemalloc.start()
start_time = time.time()

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
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.rstrip().split(',')[0][0].lower(): int(line.rstrip().split(',')[1]) for line in file if line[0].isalpha()}

def selection_sort(lst):
    '''
    selection sort algorithm 
    to make lecsicographical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''
    for i in range(len(lst) - 1, 0, -1):
        min_i = i - 1
        for j in range(i, 0, -1):
            if lst[j][0][0] < lst[min_i][0][0]:
                min_i = j
        lst[i - j], lst[min_i] = lst[min_i], lst[i - j]
    return lst


def quick_sort(lst):
    '''
    quick sort algorithm
    >>> quick_sort([('Steve Jobs', 160), \
('Albert Einstein', 160), ('Sir Isaac Newton', 195), \
('Nikola Tesla', 189)])
    [('Sir Isaac Newton', 195), ('Nikola Tesla', 189), \
('Albert Einstein', 160), ('Steve Jobs', 160)]
    '''
    if not lst:
        return []
    pivot = lst[len(lst) // 2][1]
    low = [el for el in lst if el[1] < pivot]
    high = [el for el in lst if el[1] > pivot]
    if pivot in low:
        low.append(pivot)
    else:
        high.insert(0, pivot)
    return quick_sort(low) + quick_sort(high)


def rescue_people(smarties: dict, limit_iq: int)->tuple:
    '''
    Counts the amount of travels to get people
    to another planet.

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    list_names_iq = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    all_trips = []
    trip = []
    iq_left = limit_iq
    limit_people = 5


    while iq_left > 0 and list_names_iq:
        for ind, el in enumerate(list_names_iq):
            if isinstance(el, tuple) and iq_left >= el[1]:
                trip.append(el[0])
                list_names_iq[ind] = 'flew'
                iq_left -= el[1]
                if iq_left == 0 or len(trip) == limit_people:
                    break
        all_trips.append(trip)
        list_names_iq = [tup for tup in list_names_iq if tup != 'flew']
        trip = []
        iq_left = limit_iq


    return len(all_trips), all_trips

if __name__=='__main__':
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
