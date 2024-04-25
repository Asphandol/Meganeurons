import time
start_time = time.time()

''' Functions returns first letter of every word
'''
def create_acronym(sentence: str) -> str:
    """
    str -> str
    Creates acronym

    >>> print(create_acronym("random access memory\\nAs soon As possible"))
    RAM - random access memory
    ASAP - As soon As possible
    >>> print(create_acronym("Hello my friend"))
    HMF - Hello my friend
    >>> print(create_acronym("12-3049"))
    None
    >>> create_acronym('random access memory\\n234')
    """
    if isinstance(sentence, str):
        num_list = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]
        for i, j in enumerate(sentence):
            if j in num_list:
                return
        sentence = sentence.split("\n")
        new_lst= []
        if len(sentence)>1:
            for el in sentence:
                acr = ""
                cur_sen = el.split()
                for i in cur_sen:
                    acr += i[0]
                acr = acr.upper()
                acr += " -"
                cur_sen.insert(0, acr)
                cur_sen = " ".join(cur_sen)
                new_lst.append(cur_sen)
                if sentence.index(el)!= (len(sentence)-1):
                    new_lst.append("\n")
            new_lst = "".join(new_lst)
        elif len(sentence)==1:
            for el in sentence:
                cur_sen = el.split()
                acr = ""
                for i in cur_sen:
                    acr += i[0]
                acr = acr.upper()
                acr += " -"
                cur_sen.insert(0, acr)
                new_lst.extend(cur_sen)
                new_lst = ' '.join(new_lst)
        return new_lst
    
if __name__=="__main__":
    import doctest
    print(doctest.testmod())
end_time = time.time()

print("Execution Time: ", end_time - start_time)
