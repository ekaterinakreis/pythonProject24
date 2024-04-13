# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# for x in my_list[2:3]:
#     print(*x)

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# num = []
# for i in list_1:
#     if type(i) == int or type(i) == float:
#         num.append(i)
# print('Sum of all numbers: ', sum(num))

# a_list = []
# for b in list_1:
#     if type(b) == str and 'a' in b:
#         a_list.append(b)
# print('All words with "a"', a_list)


# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int ]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])



# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
#
l1 = ['cat', 'dog', 'horse', 'cow']
# t1 = tuple(l1)
# print(type(t1))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = input('Who is in the first family? (Please enter with comma): ')
# family_2 = input('Who is in the second family? (Please enter with comma): ')
# fam1 = tuple(family_1.split(","))
# fam2 = tuple(family_2.split(','))
# if len(fam1) > len(fam2):
#     print('The first family is bigger!')
# elif len(fam1) < len(fam2):
#     print('The second family is bigger!')
# else:
#     print('The families are equal!')


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

dict1 = {'title': 'Interstellar', 'director': 'Christopher Nolan', 'year': '2014', 'budget': '$165 million',
         'main_actor': 'Matthew McConaughey', 'slogan': 'The end of Earth will not be the end of us. Go further'}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# result = 0
# for key in my_dictionary:
#     result += my_dictionary[key]
# print(result)


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# list_1 = list(set(list_1))
# print(list_1)

#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1 & set2) #пересечение множества

# print(set1.difference(set2))
# print(set1 - set2) #разные значения в set1

# print(set1.symmetric_difference(set2))
# print(set1^set2) #Симметричная разница множеств

# print(set2.issubset(set1))
# print(set1.issubset(set2))

# print(set1.issuperset(set2))
# print(set2.issuperset(set1))

#
# print(set1 <= set2)  #подмножества
# print(set2.issubset(set1)) #подмножества
