""""
https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
https://book.pythontips.com/en/latest/decorators.html
https://machinelearningmastery.com/a-gentle-introduction-to-decorators-in-python/
https://www.scaler.com/topics/python/python-decorators/
https://bytepawn.com/python-decorators-for-data-scientists.html
https://bytepawn.com/python-decorator-patterns.html#python-decorator-patterns
https://github.com/GrahamDumpleton/wrapt/blob/develop/blog/01-how-you-implemented-your-python-decorator-is-wrong.md
"""
from datetime import datetime


def func_logger(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
        print(f'{"-"*30}')
    return wrapper


@func_logger
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup()

# # Output

# Daily backup job has finished.
# Function: daily_backup
# Run on: 2021-06-06 06:54:14
# ---------------------------



# from functools import wraps
import functools

def my_decorator_func(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    print(1+2)


print(my_func(1))




def logit(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called



from time import time, sleep
    
def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took', time() - t)
    return wrapper

@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)

sleepy_function(0.3)
sleepy_function(0.5)


import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}() took {end-start:.2f} secs.")
    return inner


@timer
def test_list_append(range_limit):
    print('Start...')
    lst = [i**2 for i in range(range_limit)]
    print('Stop...')

test_list_append(1_000_000)    