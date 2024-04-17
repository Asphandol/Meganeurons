import copy

def selection_sort(lst:list) -> list:
    '''
    list -> list
    implements the selection sorting algorithm. Should return a sorted list lst
    >>> selection_sort([1,2,0,7,5])
    [0, 1, 2, 5, 7]
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5])
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    '''
    for i in range(len(lst) - 1):
        min_index = i
        min_value = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] < min_value:
                min_index = j
                min_value = lst[j]
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def quick_sort(lst:list) -> list:
    '''
    list -> list
    implements a quick sort algorithm. Should return a sorted list lst
    >>> quick_sort([('А', 23), ('Б', 8), ('В', 21), ('Г', 9), ('Ґ', 2)])
    [('Ґ', 2), ('Б', 8), ('Г', 9), ('В', 21), ('А', 23)]
    >>> quick_sort([(1, 23), (5, 8), (5, 21), (6, 9), (6, 2)])
    [(6, 2), (5, 8), (6, 9), (5, 21), (1, 23)]
    '''
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2][1]
    left = [x for x in lst if x[1] < pivot]
    middle = [x for x in lst if x[1] == pivot]
    right = [x for x in lst if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def top_names(correct_list:list, num_list:list)-> set:
    '''
    Returns top 3 names
    list, list -> set
    >>> top_names([('А', 23), ('В', 21), ('Г', 9), ('Б', 8), ('Ґ', 2)], [23, 21, 9, 8, 2]) == {'А', 'В', 'Г'}
    True

    >>> top_names([('Марія', 23), ('Ольга', 21), ('Юлія', 19), ('Катерина', 18)], [23, 21, 19, 18, 17, 16]) == {'Марія', 'Ольга', 'Юлія'}
    True

    >>> top_names([('Марія', 23), ('Ольга', 21), ('Юлія', 19), ('Катерина', 18)], [18, 19, 21, 23]) == {'Марія', 'Ольга', 'Юлія'}
    True
    '''
    sorted_list = selection_sort(num_list)[::-1][:3]
    top_list = list(map(lambda x: x[0], filter(lambda x: x[1] in sorted_list, correct_list)))
    return set(top_list[:3])


def one_use_name(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns names that were used only once
    >>> one_use_name([('А', 1), ('В', 2), ('Г', 1), ('Д', 1)])[1] == {'А', 'Д', 'Г'}
    True

    (3, {'А', 'Д', 'Г'})

    >>> one_use_name([('А', 3), ('Б', 1), ('В', 2)])[1] == {'Б'}
    True

    (1, {'Б'})
    '''
    # counter = 0
    # one_list = []
    # for name in correct_list:
    #     if name[1] == 1:
    #         counter += 1
    #         one_list.append(name[0])
    # return (counter, set(one_list))
    count = {}
    for name, freq in correct_list:
        count[name] = count.get(name, 0) + freq
    counter = sum(x == 1 for x in count.values())
    return (counter, set(name[0] for name in correct_list if count[name[0]] == 1))


def popular_letter(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns most popular letter and number of names begin with it
    '''
    list_letters = []
    list_pair = []
    for name in correct_list:
        if name[0][0] not in list_letters:
            list_pair.append([name[0][0], 1])
            list_letters.append(name[0][0])
        else:
            list_pair[list_letters.index(name[0][0])][1] += 1
    best_letter = quick_sort(list_pair)[::-1][:1][0]
    counter_kids = 0
    for name in correct_list:
        if name[0][0] == best_letter[0]:
            counter_kids += name[1]
    return (best_letter[0], best_letter[1], counter_kids)

def find_names(file_path: str) -> tuple:
    '''
    str -> tuple
    '''
    with open(file_path, "r", encoding = "utf-8") as file:
        list_of_names = file.readlines()
        correct_list =[]
        num_list = []
        for el in list_of_names:
            if len(el.strip().split("\t")) == 2:
                name_num = el.replace("(", "").replace(")","").strip().split()
                name_num[1] = int(name_num[1])
                correct_list.append(name_num)
                num_list.append(name_num[1])
    # return top_names(correct_list, num_list)
    # return one_use_name(correct_list)
    return (top_names(correct_list, num_list),one_use_name(correct_list), \
popular_letter(correct_list))



if __name__=="__main__":
    import doctest
    print(doctest.testmod())
