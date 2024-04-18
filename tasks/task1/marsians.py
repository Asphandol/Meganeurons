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
    dict_iq={}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0].isalpha():
                line=line.rstrip().split(',')
                dict_iq[line[0]]=int(line[1])
    return dict_iq

def selection_sort(lst):
    '''
    selection sort algorithm 
    to make lecsicographical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''
    ind=0
    if len(lst)>=1:
        while ind!=len(lst)-1:
            for el in range(ind+1, len(lst)):
                if lst[el][0][0]<lst[ind][0][0]:
                    lst[el], lst[ind]=lst[ind], lst[el]
            ind+=1
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
    length=len(lst)
    if length<=1:
        return lst
    pivot=lst.pop()
    low=[]
    high=[]
    for el in lst:
        if pivot[1]<el[1]:
            low.append(el)
        elif pivot[1]>el[1]:
            high.append(el)
        else:
            if pivot==selection_sort([pivot, el]):
                low.append(el)
            else:
                high.append(el)

    return quick_sort(low)+[pivot]+quick_sort(high)

def rescue_people(smarties: dict, limit_iq: int)->tuple:
    '''
    Counts the amount of travels to get people
    to another planet.

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    list_names_iq=list(smarties.items())
    list_names_iq=sorted(list_names_iq, key=lambda x: (-x[1], x[0]))
    all_trips=[]
    trip=[]

    while any(list_names_iq):
        iq_left=limit_iq
        trip=[]
        for ind, el in enumerate(list_names_iq):
            if isinstance(el, tuple) and iq_left>=el[1]:
                trip.append(el[0])
                list_names_iq[ind]='flew'
                iq_left-=el[1]
        all_trips.append(trip)
        list_names_iq=[tup for tup in list_names_iq if tup!='flew']
    return (len(all_trips), all_trips)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
