def odd_eve(l):
    odd = []
    eve = []
    for i in l:
        if i%2==0:
            eve.append(i)
        else :
            odd.append(i)
    output = [eve,odd]
    return output 

numbers = [1,2,4,3,5,6,54,2,36,43,31]
print(odd_eve(numbers))