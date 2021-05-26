def reverse(l):
    tmp = []
    for i in l:
        tmp.append(i[::-1])
    return tmp

random_strings = ['asd','zxc','qwe']
print(reverse(random_strings))