import copy
import time
start_time = time.time()


def selection_sort(lst: list) -> list:
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
    for i in range(len(lst) - 1, 0, -1):
        min_ind = j = i - 1
        for j in range(i - 1, 0 - 1, -1):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i - 1], lst[min_ind] = lst[min_ind], lst[i - 1]
    return lst

def quick_sort(lst:list) -> list:
    '''
    implements the selection sorting algorithm. Should return a sorted list lst
    >>> quick_sort([1,2,0,7,5])
    [0, 1, 2, 5, 7]
    >>> quick_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5])
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    '''
    if len(lst) > 1:
        pivot = lst[len(lst) // 2]
        smaller_list, middle_list, bigger_list = [], [], []

        for num in lst:
            if num[1] > pivot[1]:
                bigger_list.append(num)
            elif num[1] < pivot[1]:
                smaller_list.append(num)
            else:
                middle_list.append(num)
        return quick_sort(smaller_list) + middle_list + quick_sort(bigger_list)
    return lst


def top_names(correct_list:list, num_list:list)-> set:
    '''
    Returns top 3 names
    list, list -> set
    '''
    top_names = {}
    for i, name in enumerate(correct_list):
        top_names[name[1]] = i
    sorted_names = sorted(top_names.items(), key=lambda x: x[1], reverse=True)[:3]
    return {name[0] for name in sorted_names}


def one_use_name(correct_list: list) -> tuple:
    '''
    list -> tuple
    Returns names that were used only once
    '''
    return len(set([name[0] for name in correct_list if name[1] == 1])), frozenset(correct_list)


def popular_letter(correct_list: list) -> tuple:
    '''
    list -> tuple
    Returns most popular letter and number of names begin with it
    '''
    letter_count = {}
    total_count = 0
    for name in correct_list:
        letter = name[0][0]
        if letter not in letter_count:
            letter_count[letter] = 1
            total_count += name[1]
        else:
            letter_count[letter] += 1
            total_count += name[1] - 1
    max_letter, max_count = max(letter_count.items(), key=lambda x: x[1])
    return (max_letter, max_count, total_count - sum(count for letter, count in letter_count.items() if letter != max_letter))


def find_names(file_path: str) -> tuple:
    '''
    str -> tuple
    '''
    with open(file_path, "r", encoding="utf-8") as file:
        list_of_names = [line.strip().split("\t") for line in file.readlines() if len(line.strip().split()) == 2]
        correct_list = [line[0] + (int(line[1]),) for line in list_of_names]
        num_list = [int(name[1]) for name in correct_list]
    return (top_names(correct_list, num_list), one_use_name(correct_list), popular_letter(correct_list))

if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
