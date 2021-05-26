def common(l1,l2):
    tmp = []
    for i in l1:
        if i in l2:
            tmp.append(i)
    return tmp

l1 = [1,2,5,0,6,7,9,8]
l2 = [1,2,3,4,5,6,7]
print(common(l1,l2))