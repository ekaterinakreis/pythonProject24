import sys
# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# health_of_hero = int(input("Heath points: "))
# if health_of_hero <= 0:
#     print('False')
# else:
#     print('True')

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

# number = int(input('Enter your number: '))
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400,
# он также считается високосным (1200, 2000)

# year = int(input('Enter year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print('This year is leap year!')
# else:
#     print('This is regular year!')

# С вложенными условиями
# year = int(input())
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print('Високосный')
#         else:
#             print('Невисокосный')
#     else:
#         print('Високосный')
# else:
#     print('Невисокосный')

# C логическими операторами

# if not year%4 and year%100 or not year%400:
#     print('Високосный')
# else:
#     print('Невисокосный')



# # Задание 2.4
# # Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# # Текст и количество повторений нужно ввести с помощью input()
#
# text = input('Write your message: ')
# num = int(input("Enter number of reiteration: "))
# # print(f'{num} * {text}')
# for index in range (1, num+1):
#     print(text)
#     # print(index, text)

#  loop while

# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# i = 1
# while i <= num:
#     print(text)
#     i += 1

#
# word = 'hello'
# for symbol in word:
#     print(f'{word.index(symbol)} - {symbol}')
# word = 'hello'
# for index, symbol in enumerate(word):
#      print(f'{index} - {symbol}')


# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

# num1 = input('Enter first number: ')
# num2 = input("Enter second number: ")
# operator = input('Enter your operator: ')
# if operator == "+":
#     result = int(num1) + int(num2)
# elif operator == "-":
#     result = int(num1) - int(num2)
# elif operator == "*":
#     result = int(num1) * int(num2)
# elif operator == "/":
#     result = int(num1) / int(num2)
# elif operator == "**":
#     result = int(num1) ** int(num2)
# elif operator == "//":
#     result = int(num1) // int(num2)
# print(f'{num1} {operator} {num2} = {result}')

#
# def multiply_it(x, y):
#     result = x * y
#     return result
#     # yield result
#     # print('Finish')
# print(multiply_it(10, 5))


# num1 = int(input('Пожалуйста, введите первое число: '))
# num2 = int(input('Пожалуйста, введите второе число: '))
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         sys.exit()
# elif operator == '+':
#     result = num1 + num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')