import re

text = ('A palindrome is a type of wordplay involving words, phrases, or sentences that read the same backward and forward'
        'Madam, I\'m Adam'
        'A man, a plan, a canal — Panama'
        'Able was I ere I saw Elba')

pattern = r'P'
pattern1 = 'I\'m'
# . any symbol G.....   G..{3,5}
# {} diapozon {4}
# \w for unicode (str) any letter in english alphabet, lowcases and uppercases + numbers [a-zA-Z0-9_]
#  \s all symbols in [ \t\n\r\f\v] tab, \n and other
#  \d all numbers [0-9]

x = re.findall(pattern, text, flags = re.IGNORECASE)
# print(x)

# only first pattern
x1 = re.search(pattern, text, flags = re.IGNORECASE)
# print(x1)
# print(x1.start())
# print(x1.group())
# print(x1.span())


x2 = re.split(pattern, text, flags = re.IGNORECASE, maxsplit=0)
# print(x2)
# print(len(x2))

# sub is the same as replace
x3 = re.sub(pattern, 'News', text, flags = re.IGNORECASE)
print(x3)

