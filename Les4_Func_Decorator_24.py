# def sum_it(a, b, c =5):
#     return a + b + c
#
# print(sum_it(5, 4))

# pozition arguments
# def sum_it(a, b, c):
#     return a + b + c
#
# print(sum_it(5, 4, 10))

# named arg after pizition args
# print(sum_it(5, 4, c = 10))

# def hello(fname, lname, age):
#     return f'Hello, my name is {fname} {lname}. I am {age} years old'
# print(hello(25, "Anna", "Smith"))
# print(hello(age = 25, fname = "Anna", lname = "Smith"))
#
# def pattern(lenght, char1 = '/', char2 = "*"):
#     return(char1 + char2) * lenght + char1
# print(pattern(9))

# встроенные func
# min_value = min(5, 8, 1, 25,0)
# print(min_value)

# variable loookup: local, enclosed, global, build-in
# Scope

name = 'Alice'
def outer_function():
    # name = 'Alex'
    def inner_function():
        # name = 'Albert'
        return name
    return inner_function()

enclosure = outer_function()
result = enclosure
# print(result)

# Decorator
def decorator_function(func):
    def wrapper(*arg):
        print('wrapper function!')
        print(f'Wrapped function!: {func.__name__}')
        print(f"Executing wrapper func!")
        print(func(*arg))
        print('Exiting wrapper func')
    return wrapper

@decorator_function
def my_wrapper(item):
    return f'{item} is wrapped!'

# my_wrapper('Candy')

@decorator_function
def hello(name):
    return f'Hello, my name is {name}'

# hello('Alex')

x = 5
y = 10
def sum_it2(x, y):
    print(f'Locals: {locals()}')
    return x + y

# print(f'Inside the function: {sum_it2(5, 2)}')
# print(f'Outside the func: {x + y}')
# print(f'Globals: {globals()}')
# ________________________________
# Moduls
import math as m
# from math import prod
from math import *

# arr = [1, 5, 10, 25]
# result = m.prod(arr)
# print(result)

import datetime

# birth_year = 1985
# current_date = datetime.date.today()
# current_age = current_date.year - birth_year
# print(current_date)
# print(current_age)

# def introduce(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# introduce(name = 'Mario', lname = 'Smith', position = 'QA')
# ___________________________________________
# lambda - anonimoys func

res = lambda x, y: x * y
print(res(2, 5))

def take_odd(num):
    if num%2:
        return True
    return False

l = [1, 5, 8, 12, 15]
# new_l = list(filter(lambda x: x%2, l))
# print(new_l)

# new_l1 = list(filter(take_odd, l))
# print(new_l1)

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
new_l2 = list(filter(lambda a: type(a)==str and "a" in a, list_1))
# print(new_l2)

from functools import reduce
# reduce gives 1
res1 = reduce(lambda x, y: x + y, l)
print(res1)
