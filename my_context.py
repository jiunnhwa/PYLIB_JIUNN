"""
https://wiki.c2.com/?CoRoutine

"""
# https://onecompiler.com/python/3yrhkq3pc

def Lock(func, x):
  print ("Locking...") # your self.lock()
  try:
    return func(x)
  finally:
    print ("Unlocking!") # your self.unlock()

def func(x): print ( x + "... Now in func!")

Lock(func, "me")
