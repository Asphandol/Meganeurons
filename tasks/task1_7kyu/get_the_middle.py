def get_middle(s):
    if len(s) % 2 != 0: #якщо непарні
        return s[int((len(s)-1)/2)]
    else: #якщо парні
        return s[int((len(s)-2)/2)] + s[int(len(s)/2)]
