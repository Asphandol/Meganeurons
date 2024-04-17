'''Calculate expression'''
def calculate_expression(expression:str) -> int:
    '''
    >>> calculate_expression("Скільки буде 8 відняти 3 плюс 4 мінус 5 помножити на 2?")
    8
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3 додати 2?")
    11
    >>> calculate_expression("3 плюс 2")
    5
    '''
    counter_str = 0
    counter_num = 0
    num_line = '0987654321'
    opposite_line = '-'
    str_line = 'додати плюс відняти мінус поділити помножити'
    result_line = []
    if isinstance(expression,str):
        if '?' not in expression:
            return 'Неправильний вираз!'
        if 'Скільки' not in expression:
            return 'Неправильний вираз!'
        fine_expression = expression.replace('?','')
        fine_expression = fine_expression.replace('на', '')
        list_of_words = fine_expression.split()
        for i in fine_expression:
            if i in opposite_line:
                counter_num += 1
            if fine_expression[-1] not in num_line:
                return 'Неправильний вираз!'
        for j in list_of_words:
            if j in str_line:
                counter_str += 1
            elif j.isdigit():
                counter_num += 1
        if counter_str + 1 != counter_num:
            return 'Неправильний вираз!'
        if counter_num == 0:
            return 'Неправильний вираз!'
        if counter_num == 1:
            result = list_of_words.pop()
            return int(result)
        for indx,elem in enumerate(list_of_words):
            if elem == 'відняти':
                elem = int(list_of_words[indx-1]) - int(list_of_words[indx+1])
                list_of_words.remove(list_of_words[indx+1])
                list_of_words.insert(indx+1,elem)
                result_line.append(elem)
            elif elem == 'мінус':
                elem = int(list_of_words[indx-1]) - int(list_of_words[indx+1])
                list_of_words.remove(list_of_words[indx+1])
                list_of_words.insert(indx+1,elem)
                result_line.append(elem)
            elif elem == 'додати':
                elem = int(list_of_words[indx-1]) + int(list_of_words[indx+1])
                list_of_words.remove(list_of_words[indx+1])
                list_of_words.insert(indx+1,elem)
                result_line.append(elem)
            elif elem == 'плюс':
                elem = int(list_of_words[indx-1]) + int(list_of_words[indx+1])
                list_of_words.remove(list_of_words[indx+1])
                list_of_words.insert(indx+1,elem)
                result_line.append(elem)
            elif elem == 'помножити':
                elem = int(list_of_words[indx-1]) * int(list_of_words[indx+1])
                list_of_words.remove(list_of_words[indx+1])
                list_of_words.insert(indx+1,elem)
                result_line.append((elem))
            elif elem == 'поділити':
                if list_of_words[indx+1] != '0':
                    elem = int(list_of_words[indx-1]) / int(list_of_words[indx+1])
                    list_of_words.remove(list_of_words[indx+1])
                    list_of_words.insert(indx+1,elem)
                    result_line.append((elem))
                else:
                    return 'Неправильний вираз!'
        result = result_line.pop()
        return int(result)
print(calculate_expression('Скільки буде 2?'))