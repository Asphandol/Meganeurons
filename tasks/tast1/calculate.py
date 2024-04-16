''' Function calculator
'''
def calculate_expression(expression: str) -> int:
    ''' 
    str -> int
    Calculator 
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression('Скільки буде 2?')
    2
    >>> calculate_expression("Скільки 10 поділити на -2 додати 11 мінус -3?")
    'Неправильний вираз!'
    >>> calculate_expression("Скільки 10 поділити на 0 додати 11 мінус -3?")
    'Неправильний вираз!'
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    '''
    command_lst = ['додати', 'плюс', 'відняти', 'мінус', 'помножити', 'поділити']
    num_lst= []
    cur_com=[]
    res = 0
    word_lst = ["Скільки", "буде", "?"]
    if isinstance(expression, str):
        for el in word_lst:
            if el not in expression:
                return "Неправильний вираз!"
        expression = expression.replace("Скільки буде", "")
        expression = expression.replace("?", "")
        if "на" in expression:
            expression = expression.replace("на", "")
        exp_lst = expression.split()
        for el in exp_lst:
            try:
                num_lst.append(int(el))
            except ValueError:
                if el not in command_lst:
                    return "Неправильний вираз!"
        for i, j in enumerate(exp_lst):
            try:
                while i != (len(exp_lst)-1):
                    exp_lst[i]= int(exp_lst[i])
                    exp_lst[i+1]= int(exp_lst[i+1])
                # if i == (len(exp_lst)-1):
                #     continue
                # else:
                #     exp_lst[i]= int(exp_lst[i])
                #     exp_lst[i+1]= int(exp_lst[i+1])
                    return "Неправильний вираз!"
            except ValueError:
                if i == (len(exp_lst)-1):
                    continue
                if i != (len(exp_lst)-1):
                    if exp_lst[i] in command_lst and exp_lst[i+1] in command_lst:
                        return "Неправильний вираз!"
        for i, j in enumerate(exp_lst):
            if exp_lst[i] == command_lst[5] and exp_lst[i+1] == "0":
                return "Неправильний вираз!"
        for el in exp_lst:
            if el in command_lst:
                cur_com.append(el)
        res = num_lst[0]
        for i in range(len(num_lst)-1):
            if cur_com[i]==command_lst[0] or cur_com[i]==command_lst[1]:
                res += num_lst[i+1]
            elif cur_com[i]==command_lst[2] or cur_com[i]==command_lst[3]:
                res -= num_lst[i+1]
            elif cur_com[i]==command_lst[4]:
                res *= num_lst[i+1]
            elif cur_com[i]==command_lst[5]:
                res /= num_lst[i+1]
        return int(res)


