# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     return [f'Perimeter is: {a * 4}, Area is: {a ** 2}, Diagonal is: {(2 ** 0.5) * a}']
# print(square(2))

import math as m
def square(a):
    return(a*4, a**2, (round(m.sqrt(2*(a**2)), 2)))
# square_data = square(int(input("Enter size of squres`s side: ")))

# print(square(2))
# print(square(2))
# print(type(square(2)))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
def person(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}: {v}')
    #return "Hello!\n My name is: %s.\n My last name is: %s.\n I am %s years old. \n My position is: %s"%tuple(kwargs.values())
    # return "Hello!\n My name is: %s.\n My last name is: %s.\n I am %s years old. \n My position is: %s"%(kwargs.get('name'), kwargs.get('last_name'), kwargs.get('age'), kwargs.get('position'))
# print(person(name = 'John', last_name = 'Smith', age = '35', position = 'web developer'))

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

my_list = [20, -3, 15, 2, -1, -21]

# print(list(filter(lambda x: x>0, my_list)))
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
from functools import reduce
# print(reduce(lambda x, y: x*y, my_list))

# Чтобы получить результат перемножения только положительных значений
# print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import time

def counter_time(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        exec_time = end - start
        print(f'{func.__name__} ececution time is: {exec_time}')
        return result
    return wrapper

@counter_time
def square(a):
    return(a*4, a**2, (round(m.sqrt(2*(a**2)), 2)))

# square(2)
# print(square(2))

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

from my_calc import *

res1 =  sum_it(2, 5)
print(res1)

res2 = sub_it(2, 5)
print(res2)

res3 = prod(5, 5)
print(res3)

res4 = remain(11, 2)
print(res4)

res5 = div_it(66, 3)
print(res5)

res6 = div_it(66, 0)
print(res6)