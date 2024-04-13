# def myfunc(a = 5, b = 5):
#   return a + b
# print(20, 20)
#
# def myfunc(*args):
#   return sum(args)
# print(20, 20, 10, 33, 56, 100)

l1 = [1, 2, 3, 4, 5]

# print(list(map(str, l1)))
# print(list(map(lambda x: x + 2, l1)))
# print([x + 2 for x in l1])

# list or string for visualisation
# join works only with strings
# print("".join([str(x) for x in l1]))
# print(''.join(map(str, l1)))

# filter works with lambda

# sort even numbers
print(list(filter(lambda x: x % 2 == 0, l1)))
print(''.join(map(str, (filter(lambda x: x % 2 == 0, l1)))))

# list comprehension
# print(''.join(str(x) for x in l1 if x % 2 == 0))

#
# l_odd = [x for x in range(1, 101) if x % 2 != 0]
# l_even = [x for x in range(1, 101) if x % 2 == 0]
# l3 = [x for x in range(1, 101)]
#
# [l_odd.append(x) if x % 2 != 0 else l_even.append(x) for x in l3]
#
# for num in l3:
#     if num % 2 != 0:
#         l_odd.append(num)
#     else:
#         l_even.append(num)

# l4 = [1, 2, 3, 4, 5, 6, 7]
#
# def multiplier(num):
#     return num * 2
# l5 = []
# for num in l4:
#     l5.append(multiplier(num))
#
# print([multiplier(x) for x in l4])
# print(list(map(multiplier, l4)))
# print(l5)



from functools import reduce


l3 = [x for x in range(1, 101)]
l4 = [str(x) for x in range(3, 77)]
# print(l4)
#
l3.extend(l4)
l3_filtered = list(filter(lambda x: type(x) == int, l3))

print(reduce(lambda x, y : x + y, l3_filtered))
print(reduce(lambda x, y: x + y, ([x for x in l3 if type(x) == int])))

# l3_filtered = list(map(lambda x: x if type(x) == int else 0, l3))
# print(l3_filtered)

# # print([x for x in l3 if type(x) == int])

# print(reduce(lambda a, b: a + b, l3)) if l3_filtered else 0)

#
# sum_l3 = 0

# for num in l3:
#     if type(num) == int:
#         sum_l3 += num
#
# print(sum_l3)
#
# #print(l3)

