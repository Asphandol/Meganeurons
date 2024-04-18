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

if __name__=='__main__':
    import doctest
    print(doctest.testmod())