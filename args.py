def calculate(a,*args):
    if args:
        return [i**a for i in args]
    else:
        return "you didn't pass any args"

l = [1,2,3,4,5]
print(calculate(2,*l))