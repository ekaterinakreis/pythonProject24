# 1.0 Напишите и запустите программу. которая выводит строку  "Hello world!"

# print("Hello world!")

# 1.1 Напишите программу, которая на входе получает имя пользователя,
# сохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"
#
# print('Enter your name:')
# name = input()
# print(f"Hello, {name}!")

# 1.2 Напишите программу, чтобы вывести:
#
# *********
# *         *
# *          *
# *********

# star = '*'
# space = " "
# print(star*9+ '\n'+ (star + space*7 + star +'\n')*2 + star*9)

# 1.3 Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# number = int(input("Enter 4-sign: "))
# thousands = number // 1000
# hundreds = number % 1000//100
# tens = number % 100//10
# ones = number % 10
# print(f'Thousands: {thousands}')
# print(f'Hundreds: {hundreds}')
# print(f'Tens: {tens}')
# print(f'Ones: {ones}')


# 1.4 Напишите программу, которая считывает два целых числа a и b и
# выводит на экран квадрат суммы  (a+b)2 и сумму квадратов a2+b2 этих чисел.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# # c = (a + b)**2
# # d = a**2 + b**2
# # print (f'Square of the sum is: {c}')
# # print (f'Sum squared is: {d}')
# print(f"({a}+{b})**2 = {(a+b)**2}")