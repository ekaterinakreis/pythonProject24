# # LISTS
# Create a list: option 1
# l = [1, 'string', 12.3, 'Hello', 25]
# print(l)
#
# # Create a list: option 2
# sentence = 'What a wonderful life!'
# my_list = list(sentence)
# print(my_list)
# my_list1 = sentence.split(' ')
# print(my_list1)
#
# # For loop with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num*2)
# #
# # In-place list mutating
#
# l = [8, 7, 5, 10]
# print(l)
# print(id(l))
# l[0] = 0
# print((l))
# print(id(l))
#
# l1 = [25, 80]
# l.append(l1)
# print(l)
# print(id(l))
#
# # .append and .extend()
# add = 'extra'
# l.append(add)
# l1.extend(add)
# print(l)
# print(l1)
#
#
# # .sort() and sorted()
#
# nums = [2, 3, 1, 5, 6, 4, 0]
# print(f'Initial list: {nums}')
# print(id(nums))
# #
# print('SORTED()')
# print(f'New sorted list: {sorted(nums)}')
# print(f'Initial list after sorting: {nums}')
# print(id(sorted(nums)))
# print('.SORT()')
# print(f'New sorted list: {nums.sort()}')  # None
# print(f'Initial list After sorting: {nums}')
# print(id(nums))
# print(nums.reverse())
# print(nums)
# print(id(nums))
#
# # Slicing
# numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# print(numbers[0:-1:2])
# print(numbers[-3])
# print(numbers[::-1])
# print(numbers[1:-1])
#
#
# # list comprehension
# #
# l = [1, 2, 3, 4, 5]
# new_l = []
# for x in l:
#     if x%2:
#         new_l.append(x*x)
# print(new_l)
#
# new_l = [x*x for x in l if x%2]
# print(new_l)
#
# #TUPLES
# # Create a tuple: option 1
# mytuple = 1, 2, 3
# print(mytuple)
#
#
# # Create a tuple: option 2
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# print(my_tuple)
#
# name = 'Mark',
# print(name)
#
# name = ('Mark',)
# print(name)
# print(type(name))
#
# name = ('Mark')
# print(name)
# print(type(name))
#
#
# letters = ('apple', 'banana', 'cat')
# a, b, c = letters
# print(a)
# print(b)
# print(c)
#
# letters[0] = 'ananas'
# print(letters)
#
# # letters = list(letters)
# # letters[0] = 'ananas'
# # print(letters)
#
# # Getting index of items
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))
#
# # Filtering
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# result = tuple(filter(lambda x: isinstance(x, int), my_tuple))
# print(result)
#
# # Tuple methods
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tuple is: {len(my_tuple)}')
# print(f'Length of result is: {len(result)}')
#
# # Iterate tuple with for loop
# for (index, item) in enumerate(my_tuple):
#     print(index, item)
#
# # iterate tuple with while loop
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1
#
# # Nested list in tuple
# letters = ('apple', ['ananas', 'mango'], 'melon')
# letters[1][0] = 'cherry'
# print(letters)
#
# # swaping variables
# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')
#
# # Passing tuple as an argument in function
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
#
#
# def func(*args):
#     l = []
#     for item in args:
#         l.append(item*item)
#     return l
#
# print(func(2, 5, 6, 8, 10))
#
#
# #DICTIONARIES
# my_dict = {
#     'name': 'Anna',
#     'last_name': 'Pavlova',
#     'age': 30,
#     'department': 'IT'
# }
#
# print(my_dict)
# print(id(my_dict))
# print(my_dict['name'])
# my_dict['last_name'] = 'Smirnova'
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))
# my_dict['salary'] = 5000
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('name'))
#
#
# # SETS
# print(set([1, 8, 2, 1, 5, 8, 9]))
#
# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
#
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# print(set1.remove(1))
# print(set1)
# print(set1.add(8))
# print(set1)
#
# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)
#
# fs.add(4)
# print(fs)
