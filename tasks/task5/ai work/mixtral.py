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
    '''
    if len(lst)>1:
        el = lst[len(lst) // 2]
        smaller_list = []
        bigger_list = []
        middle_list = []
        for num in lst:
            if num[1] > el[1]:
                bigger_list.append(num)
            elif num[1]<el[1]:
                smaller_list.append(num)
            elif num[1] == el[1]:
                middle_list.append(el)
        return quick_sort(smaller_list) +middle_list+ quick_sort(bigger_list)
    return lst


def top_names(correct_list:list, num_list:list)-> set:
    '''
    Returns top 3 names
    list, list -> set
    '''
    sorted_list = selection_sort(num_list)[::-1][:3]
    top_list = []
    for name in correct_list:
        if name[1] in sorted_list:
            top_list.append(name[0])
    return set(top_list[:3])


def one_use_name(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns names that were used only once
    '''
    counter = 0
    one_list = []
    for name in correct_list:
        if name[1] == 1:
            counter += 1
            one_list.append(name[0])
    return (counter, set(one_list))


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
