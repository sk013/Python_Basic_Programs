def decorative_fun(tmp_function):
    def random_function(*args, **kwargs):
        print("this is decorative part")
        return tmp_function(*args, **kwargs)
    return random_function

@decorative_fun
def fun1():
    print("this is function 1")

@decorative_fun
def fun2():
    print("this is function 2")

@decorative_fun
def fun3(a,b):
    return a+b

fun1()
fun2()
print(fun3(43,34))