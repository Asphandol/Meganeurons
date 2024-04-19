import re
import time
start_time = time.time()
from collections import defaultdict, Counter

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
    n = len(lst)

    for step in range(n):
        min_idx = step
        for i in range(step+1, n):
            if lst[min_idx] > lst[i]:
                min_idx = i
        lst[step], lst[min_idx] = lst[min_idx], lst[step]

    return lst


def quick_sort(lst:list) -> list:
    '''
    list -> list
    implements a quick sort algorithm. Should return a sorted list lst
    '''
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    i = 0
    j = len(lst) - 1

    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]

    return quick_sort(lst[:i]+lst[i+1:])


def top_names(correct_list:list, num_list:list)-> set:
    '''
    Returns top 3 names
    list, list -> set
    '''
    sorted_num_list = selection_sort(num_list)[::-1][:3]
    topi_names = []
    names_to_sort = [name for name in correct_list]

    for _ in range(3):
        max_name_index = names_to_sort.index((lambda name: name[1] == sorted_num_list.pop()))
        topi_names.append(correct_list[max_name_index][0])

    return set(topi_names[:3])


def one_use_name(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns names that were used only once
    '''
    count = defaultdict(int)

    for name in correct_list:
        count[name[0]] += name[1]

    used_only_once = {name: count[name] for name, count in count.items() if count[name] == 1}
    number_of_used_only_once = len(used_only_once)

    return (number_of_used_only_once, set(used_only_once.keys()))


def popular_letter(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns most popular letter and number of names begin with it
    '''
    letter_count = Counter([name[0][0] for name in correct_list])
    most_popular_letter = letter_count.most_common(1)[0][0]
    counter_kids = sum([1 for name in correct_list if name[0][0] == most_popular_letter])

    return (most_popular_letter, letter_count[most_popular_letter], counter_kids)

def find_names(file_path: str) -> tuple:
    '''
    str -> tuple
    '''
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        correct_list = []
        num_list = defaultdict(int)

        for line in lines:
            if len(line.strip()) > 0:
                name, count = re.split(r'\s{2,}', line.strip())
                name, count = name.strip(), int(count)
                correct_list.append((name, count))
                num_list[name] += count

        top, one, popular = (
            top_names(list(correct_list), list(num_list.keys())),
            one_use_name(correct_list),
            popular_letter(correct_list)
        )
        return (top, one, popular)



if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)