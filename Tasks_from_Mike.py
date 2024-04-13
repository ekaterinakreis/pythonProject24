# l1 = [(66, 674, 38), (88, 450, 78), (59, 599, 32), (59, 600, 33), (60, 800, 43), (88, 555, 38), (55, 585, 38)]
# l2 = []
# for i in l1:
#     if i[0] < 60 and i[1]<600 and i[2]<40:
#         l2.append("Нужный Боец")
#     else:
#         l2.append("Майку Крышка")
# print(l2)

#even or odd eith slicing
# a = list(range(1, 100))
#
# for num in range(0, 101, 2):
#     print(num)


# Lists comprehension логика наоборот
# l = [1, 2, 3, 4, 5]
# l2 = [num * 2 for num in l]
# #
# # for loop
# for num in l:
#     if num % 2 == 0:
#         l2.append(num * 2)
#     else:
#         l2.append(num * 10)
# print(l2)
# l2 = [num * 2 if num % 2 == 0 else num * 10 for num in l]


# # type and isinstance
# list = ['apple', 12, 5.6, 'Banana', 'Apricot', 'Orange', False,
#         66, 1989, 'Pear', 'Avocado', 'grape', 'aston villa']
# new_list = []
# for item in list:
#     if isinstance(item, str) and item[0].lower() == 'a':
#         new_list += [item]
# print(new_list)

# new_list2 = []
# for item in list:
#     if type(item) == str and item[0].lower() == 'a':
#         new_list2.append(item)
# print(new_list2)


# print(["Andrew", "Mike"][True])
# print(["Andrew", "Mike"][1])





