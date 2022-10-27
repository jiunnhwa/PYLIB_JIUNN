# -------------------------------------------------------------
"""
Using clousures to properly replace case
https://www.codeforests.com/2020/08/01/python-closure-real-world-examples/

"""
import re
paragraph = 'To start Python programming, you need to install python and configure PYTHON env.'
def replace_case(word):
    def replace(m):
        text = m.group()
        if text.islower():
            return word.lower()
        elif text.isupper():
            return word.upper()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(paragraph)
print(re.sub("python", "java", paragraph, flags=re.I))
print(re.sub("python", replace_case("java"), paragraph, flags=re.IGNORECASE))
# To start Python programming, you need to install python and configure PYTHON env.
# To start java programming, you need to install java and configure java env.
# To start Java programming, you need to install java and configure JAVA env.


# -------------------------------------------------------------
"""
word counter
"""
def word_counter():
    counter = {}
    def count(word):
        counter[word] = counter.get(word, 0) + 1
        return counter[word]
    return count

counter = word_counter()
print(counter('Hello World Hello    '))    


# -------------------------------------------------------------
"""
https://www.pythontutorial.net/advanced-python/python-closures/
"""

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


# multipliers = []
# for x in range(1, 4):
#     multipliers.append(multiplier(x))
multipliers = []
[multipliers.append(multiplier(x)) for x in range(1, 4)]

m1, m2, m3 = multipliers

print(m1.__closure__)
print(m1.__code__.co_freevars)
print(m1(10)) 
print(m2(10))
print(m3(10))
# (<cell at 0x000001D822A3B7C0: int object at 0x000001D8228A00F0>,)
# ('x',)
# 10
# 20
# 30



# -------------------------------------------------------------
"""
https://github.com/milaan9/07_Python_Advanced_Topics/blob/main/003_Python_Closure.ipynb
https://www.bogotobogo.com/python/python_closure.php

"""

import requests

def request_get(url):
    def print_header(**headers):
        print("headers:")
        for header in headers:
            print(header,":", headers[header])
            
    def make_request(**kwargs):
        _url = url.format_map(kwargs)
        print('url:',_url)
        print_header(**kwargs)
        # return requests.get(url.format_map(kwargs))
        return requests.get(_url)
    return make_request

# postman = request_get(r'https://postman-echo.com/get?{key}={val}')
# result = postman(key='foo',val='bar')
# print(result)

# postman = request_get(r'https://swapi.dev/api/{key}/{val}')
# result = postman(key='starships',val='9')
# print(result)


# -------------------------------------------------------------
"""
Closure func to print initial+var
"""
def print_msg(hello):
    def printer(msg):
        print(hello, msg)
    return printer  

def print_msg_lamda(hello):
    return lambda msg: f"{hello} {msg}"

print_hello = print_msg("Hello")
print_hello('World')
# Hello World

print_hello = print_msg_lamda("Hello")
print(print_hello("World"))
# Hello World


# -------------------------------------------------------------
"""
Adder
"""
def msg_adder(hello):
    def adder(msg):
        nonlocal hello
        hello += msg
        return hello 
    return adder  

words = msg_adder("A")
print(words ('B'))
print(words ('C'))



# -------------------------------------------------------------
