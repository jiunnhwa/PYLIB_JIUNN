"""
https://realpython.com/python-namedtuple/#:~:text=Python's%20namedtuple%20was%20created%20to,code%20cleaner%20and%20more%20maintainable.
https://death.andgravity.com/namedtuples
https://datagy.io/python-namedtuple/
https://miguendes.me/everything-you-need-to-know-about-pythons-namedtuples


# Understanding the namedtuple() Function
from collections import namedtuple
namedtuple(
    typename,           # The type name to be used for the tuple
    field_names,        # The field names to be used
    rename=False,       # Whether to automatically rename reserved names
    defaults=None,      # Whether to include default values
    module=None         # Whether to assign a custom module value
)



"""


from collections import namedtuple


"""
=============================================================
named tuple
=============================================================
"""
Employee = namedtuple("Employee", "ID Name Role", defaults=['Coder']) #from rightmost, non-defaulted means mandatory
John = Employee("001", "John", ["CEO"])
Jane = Employee("002", "Jane")
print(John)
print( id(John.Role))
John.Role.append ("CTO")
print(John)
print( id(John.Role))

print(Jane, id(Jane))
Jane = Jane._replace(Role='Analyst')
print(Jane, id(Jane))
print(Jane._asdict())


# -------------------------------------------------------------



"""
=============================================================
Reading from csv to named tuple
=============================================================
"""

import csv
from collections import namedtuple
News = namedtuple("News", "title url")
with open("data_news.csv", "r") as csv_file:
     reader = csv.reader(csv_file)
     Employee = namedtuple("News", next(reader), rename=True)
     for row in reader:
         item = News(*row)
         print(item.title, item.url)


# -------------------------------------------------------------
