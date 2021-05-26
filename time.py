from functools import wraps
import time

def decorative_function(tmp_function):
    @wraps(tmp_function)
    def random_function(*args, **kwargs):
        t1 = time.time()
        returned_value = tmp_function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'time taken to run {tmp_function.__name__} is {total_time} seconds')
        return returned_value
    return random_function

@decorative_function
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(10000)