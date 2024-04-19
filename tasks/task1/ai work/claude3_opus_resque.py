import time
import tracemalloc

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
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1]) for line in file if line[0].isalpha()}

def selection_sort(lst):
    '''
    selection sort algorithm 
    to make lecsicographical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''
    sorted_lst = []
    while lst:
        min_item = min(lst, key=lambda x: x[0])
        sorted_lst.append(min_item)
        lst.remove(min_item)
    return sorted_lst

def quick_sort(lst):
    '''
    quick sort algorithm
    >>> quick_sort([('Steve Jobs', 160), \
('Albert Einstein', 160), ('Sir Isaac Newton', 195), \
('Nikola Tesla', 189)])
    [('Sir Isaac Newton', 195), ('Nikola Tesla', 189), \
('Albert Einstein', 160), ('Steve Jobs', 160)]
    '''
    if len(lst) <= 1:
        return lst
    pivot = lst.pop()
    low = [el for el in lst if el[1] > pivot[1] or (el[1] == pivot[1] and el[0] < pivot[0])]
    high = [el for el in lst if el[1] < pivot[1] or (el[1] == pivot[1] and el[0] > pivot[0])]
    return quick_sort(low) + [pivot] + quick_sort(high)

def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    '''
    Counts the amount of travels to get people
    to another planet.

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    list_names_iq = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    all_trips = []
    while list_names_iq:
        iq_left, trip = limit_iq, []
        for name, iq in list_names_iq:
            if iq_left >= iq:
                trip.append(name)
                iq_left -= iq
        all_trips.append(trip)
        list_names_iq = [item for item in list_names_iq if item[0] not in trip]
    return len(all_trips), all_trips

if __name__=='__main__':
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
