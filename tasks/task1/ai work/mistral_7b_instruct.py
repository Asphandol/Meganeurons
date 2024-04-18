'''Rescue Mission'''
import time
import tracemalloc
import random
import pandas as pd


tracemalloc.start()
start_time = time.time()

def read_file(file_path: str) -> dict:
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
    # Use pandas library to read the CSV file and store the data in a numpy array
    df = pd.read_csv(file_path, header=None, names=['Name', 'IQ'], engine='python')
    # Convert the numpy array to a dictionary
    result = dict(df.to_numpy())

    return result

def selection_sort(lst: list) -> list:
    '''
    Selection sort algorithm
    to make lexical order.

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''
    n = len(lst)

    # We loop through the list until the end and maintain the index of the minimum element
    for i in range(n):
        min_idx = i

         # We find the index of minimum element in the unsorted part of the list i, j
        for j in range(i+1, n):
            # If the current element's IQ is less than
            # the minimum element's IQ, update the minimum index
            if lst[j][0] < lst[min_idx][0] or \
            (lst[j][0] == lst[min_idx][0] and lst[j][1] < lst[min_idx][1]):
                min_idx = j

        # Swap(lst[i], lst[min_idx])
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def quick_sort(arr: list) -> list:
    '''
    This function implements the quicksort algorithm
    to sort a list of tuples, where each tuple contains a name
    and an IQ value, making lexical order while considering both fields.

    The algorithm partitions the array into subarrays,
    which are sorted recursively using the base case.

    Base case: When the length of the array is less
    than or equal to one, it is already sorted and may be returned directly.

    The given algorithm performs the following steps:
    1. Choose a random pivot index and swap the pivot with the last element of the array.
    2. Initialize empty lists 'low' and 'high' for left and right subarrays.
    3. Iterate through the array starting from the
    first index, comparing each element with the pivot.
    4. While the loop condition is true, add elements less
    than pivot to the low list and increment the index,
    or add elements greater than pivot to the high list and continue the loop.
    5. Recursively call quick sort function for both the low and high subarrays.
    6. Concatenate the results from low, the last
    pivot value, and the high subarrays to obtain the sorted array.

    Example usage:

    >>> selection_sort([('Steve Jobs', 160), ('Albert Einstein', 160), ('Beyonce', 160)])
    [('Albert Einstein', 160), ('Beyonce', 160), ('Steve Jobs', 160)]
    '''

    # Base case, no need to sort arrange a single element or empty list
    if len(arr) <= 1:
        return arr

    # Randomly choose the pivot
    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]
    arr.pop(pivot_index)

    # Initialize empty lists for the left (low) and right (high) subarrays
    low, high = [], []
    i = 0

    # Traverse the partitioned array and assign elements to the correct subarray (low or high)
    while i < len(arr) - 1:

        # Add elements less than pivot to the left subarray and increment the index
        if i < len(arr) and arr[i][1] < pivot[1]:
            low.append(arr[i])

        # Add elements greater than pivot to the right subarray and continue the loop
        elif i < len(arr) and arr[i][1] > pivot[1]:
            high.append(arr[i])

        i += 1

    # Recursive calls to sort the subarrays 'low' and 'high'
    return quick_sort(low) + arr[:i+1] + quick_sort(high)


def rescue_people(smarties: dict[str, int], limit_iq: int) -> tuple[int, list[list[str]]]:
    '''
    This function simulates the rescue mission
    where people are selected based on their IQ (Intelligence Quotient)
    and the number of travels required to accommodate all selected individuals.

    Given a dictionary containing the names and their respective IQs,
    this function selects the individuals
    to be rescued in each travel based on the given limit_iq (Intelligence Quotient Limit)

    The returned tuple consists of:
    1. Number of travels required to rescue all individuals.
    2. A list of lists containing the names of individuals in each travel.

    Example usage:

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])

    Function Definition:
    '''
    # Sort the dictionary in descending order based on the IQ values,
    # using the sorted() function and lambda function as the key
    smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))

    # Initialize empty lists for the each travel's passengers and the all_trips list
    all_trips = []
    taken = []

    # Set the remaining IQ limit for the rescue mission
    iq_left = limit_iq

    # While there are still individuals to be rescued:
    while smarties:
        # Get the next individual having the highest IQ that meets the IQ limit
        x = next((x for x in smarties if iq_left >= x[1]), (None, None))

        # If no individual is found with an IQ greater or equal to the IQ limit,
        # we continue the loop, updating the IQ limit for the next reservation round
        if x[0] is None:
            all_trips.append(taken[:])
            taken = []
            iq_left = limit_iq
            continue

        # Select the individual and add their name to the taken list
        taken.append(x[0])

        # Remove the individual from the smarties dictionary
        smarties.remove(x)

        # Deduct the individual's IQ from the total remaining IQ for the rescue mission
        iq_left -= x[1]

    # Once all individuals are rescued, we add the last taken list to the all_trips list
    if taken:
        all_trips.append(taken[:])

    # The final tuple consists of the count of all travels and the list of all_trips
    return len(all_trips), all_trips


if __name__=='__main__':
    import doctest
    print(doctest.testmod())

end_time = time.time()

print("Execution Time: ", end_time - start_time)
