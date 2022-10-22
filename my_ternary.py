"""

https://flexiple.com/python/python-ternary/


"""



text = """
I came, I saw.
"""
keyword = "came"
print(('ok', 'ko' )[text is None or keyword not in text])