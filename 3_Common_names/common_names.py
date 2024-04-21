"""
Functions that makes 
"""
def common_names(female_names: list, male_names: list) -> set:
    """
    list, list -> set
    Returns, based on the analysis of lists of male and female names, 
    a set of names that are suitable for both boys and girls and begin with a vowel letter.
    >>> common_names(names_read('male.txt'),names_read('female.txt'))
    {'Ira', 'Ikey', 'Edie', 'Alix', 'Andie', 'Andy', 'Angel', 'Andrea', 'Emmy', 'Aubrey', 'Abby', \
'Adrian', 'Esme', 'Angie', 'Ariel', 'Isador', 'Abbie', 'Alex', 'Alexis', 'Ajay', 'Ike', \
'Ollie', 'Augustine', 'Elisha', 'Allyn', 'Alfie', 'Evelyn', 'Isa', 'Isadore', 'Eddy', \
'Eddie', 'Erin', 'Ali', 'Adrien', 'Abbey', 'Allie', 'Addie', 'Averil', 'Austin', \
'Ashley'}
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
    >>> 
    """
    with open(file_name, 'r', encoding="UTF-8") as content:
        return content.read().split('\n')
