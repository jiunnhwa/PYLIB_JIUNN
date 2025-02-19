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

def func_caller(func):
    import functools
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__ + " called with", "args:", args, "kwargs:", kwargs)
        return func(*args, **kwargs)
    return inner

@func_caller
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


def timer(func):
    def inner(*args, **kwargs):
        import time
        from datetime import datetime
        start = time.perf_counter()
        start_time = datetime.now()
        print(f'\n{"-"*30} START: {func.__name__}() at {start_time} {"-"*30}\n\n')
        func(*args, **kwargs)
        end = time.perf_counter()
        end_time = datetime.now()
        print(f'\n\n{"-"*30} METRICS: {"-"*30}')
        print(f"start_time: {start_time}")
        print(f"func_name: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        print(f"end_time: {end_time}")
        print(f"Elapsed: {end-start:.4} secs.")
        print(f'{"-"*30} END: {func.__name__}() at {datetime.now()} {"-"*30}\n')
    return inner


@timer
@func_caller #placed nearest to def
def test_list_append(range_limit):
    lst = [i**2 for i in range(range_limit)]
test_list_append(1_000_000)    


test_list_append(10)    
# ------------------------------ START: test_list_append() at 2022-10-27 17:14:13.186839 ------------------------------
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# start_time: 2022-10-27 17:14:13.186839
# func_name: test_list_append
# args: (10,)
# kwargs: {}
# end_time: 2022-10-27 17:14:13.187847
# Elapsed: 0.0003649 secs.
# ------------------------------ END: test_list_append() at 2022-10-27 17:14:13.187847 ------------------------------




#
# // Timer decorator func
#

def timer(func):
    '''
    decorator function to measure time of execution
    https://realpython.com/python-timer/
    https://pynative.com/python-convert-seconds-to-hhmmss/    
    https://www.geeksforgeeks.org/time-perf_counter-function-in-python/
    https://superfastpython.com/time-time-vs-time-perf_counter/
    https://builtin.com/articles/timing-functions-python
    '''
    import functools
    import time
    from datetime import timedelta,datetime

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = datetime.now()
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        end_time  = datetime.now()
        toc  = time.perf_counter()
        elapsed_time = toc  - tic
        print(f"start_time:{start_time} end_time:{end_time}")
        # print(f"Elapsed time: {elapsed_time:0.4f} seconds. (Timedelta in hh:mm:ss is {timedelta(seconds=elapsed_time)})")
        print(f"Elapsed time is {timedelta(seconds=elapsed_time)} ({elapsed_time:0.4f} seconds {(elapsed_time/60):0.4f}) minutes.")
        return value
    return wrapper_timer
