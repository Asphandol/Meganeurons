import time
start_time = time.time()

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
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def quick_sort(lst:list) -> list:
    '''
    list -> list
    implements a quick sort algorithm. Should return a sorted list lst
    '''
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    smaller_list = [x for x in lst if x[1] < pivot[1]]
    middle_list = [x for x in lst if x[1] == pivot[1]]
    bigger_list = [x for x in lst if x[1] > pivot[1]]
    return quick_sort(smaller_list) + middle_list + quick_sort(bigger_list)


def top_names(correct_list:list, num_list:list)-> set:
    '''
    Returns top 3 names
    list, list -> set
    '''
    sorted_list = sorted(num_list, reverse=True)[:3]
    return {name[0] for name in correct_list if name[1] in sorted_list}


def one_use_name(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns names that were used only once
    '''
    one_list = [name[0] for name in correct_list if name[1] == 1]
    return (len(one_list), set(one_list))


def popular_letter(correct_list:list) -> tuple:
    '''
    list -> tuple
    Returns most popular letter and number of names begin with it
    '''
    letter_counts = {}
    for name in correct_list:
        letter = name[0][0]
        if letter not in letter_counts:
            letter_counts[letter] = [1, name[1]]
        else:
            letter_counts[letter][0] += 1
            letter_counts[letter][1] += name[1]
    best_letter = max(letter_counts, key=lambda x: letter_counts[x][0])
    return (best_letter, letter_counts[best_letter][0], letter_counts[best_letter][1])

def find_names(file_path: str) -> tuple:
    '''
    str -> tuple
    '''
    with open(file_path, "r", encoding = "utf-8") as file:
        list_of_names = file.readlines()
        correct_list = []
        num_list = []
        for el in list_of_names:
            if len(el.strip().split("\t")) == 2:
                name, num = el.replace("(", "").replace(")","").strip().split()
                correct_list.append([name, int(num)])
                num_list.append(int(num))
    return (top_names(correct_list, num_list), one_use_name(correct_list), 
            popular_letter(correct_list))


if __name__=="__main__":
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
