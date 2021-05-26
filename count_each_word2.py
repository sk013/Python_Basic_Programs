def counting(s):
    tmp = {}
    for i in s:
        tmp[i] = s.count(i)
    return tmp

print(counting('qwerqwasdf'))