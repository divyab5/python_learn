# sequences :
# diff b/w list and tuple
# list is unsafe and tuple is safe

# Theory:
# we can create list in python using square brackets ```[]```and constructorb```list()```
# list will maintain insertion order
# list allows duplicate values even
# list is mutable

# Task 1: Create a list and pass some elements/items to it
# Syntax: l1 = [element1, element2, element3, element4 ...]
# Note: The elements can be any type
l1 = [10, 10.5, 'Hello', True, 20, 30, 40, 10, 20, 10]
print(l1)  # [10, 10.5, 'Hello', True, 20, 30, 40, 10, 20, 10]

l2 = list([10, 10.5, 'Hello', True, 20, 30, 40, 10, 20, 10])
print(l2)

# TypeError: list expected at most 1 argument, got 10

# Task 2: Create a list and call its positions/index : /elements/items
l3 = [10, 20, 30, 40, 50, 10, 10, 40, 60]
#      1   2   3   4   5   6   7   8   9  : length
#      0   1   2   3   4   5   6   7   8  ...positions
#     -9  -8  -7  -6  -5  -4  -3  -2   -1 ...positions
print(len(l3))  # 9
# Syntax: l3[position]
print(l3[4], l3[7])  # 50 40
print(l3[-5], l3[-2])

# Task 3: If we have duplicate values in list, weather they share same memory or different memory
# build in func: id()
l4 = [10, 20, 30, 40, 50, 10, 10, 40, 60]
#      1   2   3   4   5   6   7   8   9  : length
print(id(l4[0]), id(l4[6]), id(l4[4]))  # 4401486272 4401486272

# Task 4: Slicing
l5 = [10, 20, 30, 40, 50, 10, 10, 40, 60]
#      1   2   3   4   5   6   7   8   9  : length
#      0   1   2   3   4   5   6   7   8  ...positions
#     -9  -8  -7  -6  -5  -4  -3  -2   -1 ...positions
# Syntax: l[start: end(-1) : step-over (default value is 1]
print(l5[3: 7: 1])  # [40, 50, 10, 10]
print(l5[2:5:1])
print(l5[1:6])  # [20, 30, 40, 50, 10]
print(l5[1: 8: 2])  # [20, 40, 10, 40]
print(l5[1: 8: 3])  # [20, 50, 40]

print(l5[::])  # [10, 20, 30, 40, 50, 10, 10, 40, 60]
print(l5[:5])  # [10, 20, 30, 40, 50]
print(l5[4:])  # [50, 10, 10, 40, 60]
print(l5[::3])  # []

print(l5[-2: -5: 1])  # []
print(l5[-2: -5: -1])  # [40, 10, 10]
print(l5[-5: -2: 1])  # [50, 10, 10]

# Task 5: (Concatenating list objects) :Create two list and add it (control statements and functions, lambda functions or advance functions, comprehensions)
l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50, 60, 70]
print(l1 + l2)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60, 70]
# print(l1 * l2)  # TypeError: can't multiply sequence by non-int of type 'list'

# Task 6: Repetition
print(l1 * 2)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
print(l1 * 4)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# Task 7: Packing
# a, b, c, d, e, f, g, h, i = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(a, c, f, h)  # 10 30 60 80

a, b, *c, d = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a, b, c, d)  # 10 20 [30, 40, 50, 60, 70, 80] 90
# ValueError: too many values to unpack (expected 4)















