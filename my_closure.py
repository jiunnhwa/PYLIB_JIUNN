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
"""
https://onecompiler.com/python/3ym5x7van
"""

text_no_if = """
<TestFixture()> Public Class ClassA
    Inherits GenericBaseTest
End Class    
"""
text_if = """
#If NUNIT3 Then
<TestFixture()> Public Class Class_If_Nunit
End Class
#Else
<TestFixture()> Public Class Class_Else_Nunit
End Class
#End If
"""
text_if_not = """
#If not NUNIT3 Then
<TestFixture()> Public Class Class_If_Not_Nunit
End Class
#Else
<TestFixture()> Public Class Class_If_Not_Nunit_Else
End Class
#End If
"""
text_no_else = """
#If NUNIT3 Then
<TestFixture()> Public Class Class_If_Nunit_No_Else
End Class
#End If
"""

def get_nunit_active_class(hasdefineconst):
    """
    extract active class name based on presence of nunit compilation defines.
    """

    def get_class_name(txt):
        val = txt.strip().split("End Class")[0].split(' Class ')[1]
        return val.strip()

    def post_process(txt):
        return txt.replace("#End If", "").strip()

    def inner(text):
        val = ""
        if "TestFixture" not in text:
            return val
        # cases with #if and #Else
        if "#If NUNIT3" in text and "#Else" in text:
            parts = text.split("#Else")
            if hasdefineconst:
                val = get_class_name(parts[0])
            else:
                val = get_class_name(parts[1])
            return post_process(val)

        # without #Else
        if "#If NUNIT3" in text and "#Else" not in text:
            if hasdefineconst:
                val = get_class_name(text)
            else:
                val = ""
            return post_process(val)

        # containing #if not
        if "#If not NUNIT3" in text and "#Else" in text:
            parts = text.split("#Else")
            if hasdefineconst:
                val = get_class_name(parts[1])
            else:
                val = get_class_name(parts[0])
            return post_process(val)

        # cases without #if
        return get_class_name(text).split("Inherits")[0].strip()

    return inner

if __name__ == "__main__":
    define_constants = ['A', 'B', 'NUNIT3']
    has_nunit =  get_nunit_active_class('NUNIT3' in define_constants)
    
    print("text_no_if:",has_nunit(text_no_if))
    print("text_if:",has_nunit(text_if))
    print("text_if_not:",has_nunit(text_if_not))
    print("text_no_else:",has_nunit(text_no_else))


# -------------------------------------------------------------

