def f(s):
    '''
    The function returns the number of occurrences of each character in the given string s.
    :param s: str
    :return: dict
    '''
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r