"""
https://realpython.com/python-namedtuple/#:~:text=Python's%20namedtuple%20was%20created%20to,code%20cleaner%20and%20more%20maintainable.
https://death.andgravity.com/namedtuples

"""


from collections import namedtuple


"""
=============================================================
"""
Employee = namedtuple("Employee", "ID Name Role")
John = Employee("001", "John", ["CEO"])

print(John)
print( id(John.Role))

John.Role.append ("CTO")
print(John)
print( id(John.Role))

# -------------------------------------------------------------