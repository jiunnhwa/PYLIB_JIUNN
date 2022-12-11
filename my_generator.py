"""
https://arpitbhayani.me/blogs/fsm

"""
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fgen = fib()
print([next(fgen) for _ in range(10)])