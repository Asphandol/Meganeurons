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
        for line in (line for line in file if line[0].isalpha()):
            line = line.strip().split(',')
            dict_iq[line[0]] = int(line[1])
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

if __name__=='__main__':
    import doctest
    print(doctest.testmod())