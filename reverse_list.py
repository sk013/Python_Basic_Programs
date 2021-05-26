# def reverse(l):
#      return l[::-1]

def reverse(l):
    tmp = []
    for i in range(len(l)):
        tmp.append(l.pop())
    return tmp


numbers = list(range(1,11))
print(reverse(numbers))