# Dictionary

dict = {
    'hello': 2,
    'world': 2,
    'python': 2,
    'is': 1,
    'awesome': 1
}

# char == key; +1 = value
a = "fvbfuvbfuvufvbfubvfuvfuhsuushcud"
mydict = {}

# for char in a:
#     if mydict.get(char):
#         mydict[char] += 1
#     else:
#         mydict[char] = 1
# print(mydict)

# count how many values
# for char in a:
# 	mydict[char] = mydict.get(char, 0) +1
# for k, v in mydict.items():
# 	if v > 2:
# 		print(k, v)

# dictionary comprehension
# mydict2 = [(k, v) for k, v in {k: (a.count(k)) for k in a}.items() if v < 3]
# print(mydict2)


# dictionary with index/slicing
#mydict1 = {"David":[1, 2, 3]}
# print(mydict1["David"][-1])

# lst = [1,2,2,3,3,3,4,3,3,3,2,2,1]
#
# my_dict = [k for k, v in { k: (lst.count(k)) for k in lst}. items() if v % 2]
# print(*my_dict)
