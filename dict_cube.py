def cube(num):
    d = {}
    for i in range(1,num+1):
        d[i] = i**3
    return d

num = int(input("Enter a number "))
print(cube(num))