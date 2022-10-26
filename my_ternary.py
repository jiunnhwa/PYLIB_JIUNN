"""

https://flexiple.com/python/python-ternary/


"""



# ------------------------------------------------------------
"""
https://onecompiler.com/python/3yk6ezpct
"""
nice = True
personality = ("mean", "nice")[nice]
print("The stranger is", personality)
# The stranger is nice


is_nice = [True, False, None]
# state = "nice" if is_nice else "not nice"
# state = "none" if is_nice is None else "nice" if is_nice else "not nice"
for x in is_nice:
  state = "nice" if x else "not nice" if x is False else "none"
  print(state)

  
# ------------------------------------------------------------
text = """
I came, I saw.
"""
keyword = "came"
print(('ok', 'ko' )[text is None or keyword not in text])
