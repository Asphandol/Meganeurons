"""
Functions that makes 
"""
def common_names(female_names: list, male_names: list) -> set:
    """
    list, list -> set
    Returns, based on the analysis of lists of male and female names, 
    a set of names that are suitable for both boys and girls and begin with a vowel letter.
    >>> common_names(['Abagael', 'Abagail', 'Abbe', 'Abbey', 'Abbi', \
'Abbie', 'Abby', 'Abigael', 'Abigail', 'Abigale', 'Abra', 'Acacia', \
'Ada', 'Adah', 'Adaline', 'Adara', 'Addie'], ['Aamir', 'Aaron', \
'Abbey', 'Abbie', 'Abbot', 'Abbott', 'Abby', 'Abdel', 'Abdul', \
'Abdulkarim', 'Abdullah', 'Abe', 'Abel', 'Abelard', 'Abner', 'Abraham', \
'Abram'])=={'Abbey', 'Abbie', 'Abby'}
    True
    """
    alphabet = ['A', 'E', 'I', 'O', 'U', 'Y']
    sets = set()
    for j in range(len(male_names)-1):
        if male_names[j] in female_names and male_names[j][0] in alphabet:
            sets.add(male_names[j])
    return sets

def names_read(file_name:str) -> list:
    """
    str -> list
    Takes a file and converts into list of names
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _=tmpfile.write('Laurianne\\n\
Laurice\\n\
Laurie\\n\
Lauryn\\n\
Lavena\\n\
Laverna\\n\
Laverne\\n\
Lavina\\n\
Lavinia\\n\
Lavinie\\n\
Layla\\n\
Layne\\n\
Layney')
    >>> with open(tmpfile.name, mode='r', encoding='utf-8') as tmpfile:
    ...     print(names_read(tmpfile.name))
    ['Laurianne', 'Laurice', 'Laurie', 'Lauryn', 'Lavena', 'Laverna', \
'Laverne', 'Lavina', 'Lavinia', 'Lavinie', 'Layla', 'Layne', 'Layney']
    """
    with open(file_name, 'r', encoding="UTF-8") as content:
        return content.read().split('\n')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
