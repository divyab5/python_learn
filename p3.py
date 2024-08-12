# Theory:
# We can create tuple using parenthesis ```()``` and object ```tuple()```
# In Tuple we can pass duplicate elements, and it maintains insertion order
# Tuple is immutable (Tuple is safe)

# Task 1: Create Tuple
t1 = 10
print(t1, type(t1))   # 10 <class 'int'>

t2 = 10,
print(t2, type(t2))  # (10,) <class 'tuple'>

t3 = 10, 20, 30
print(t3, type(t3))  # (10, 20, 30) <class 'tuple'>

t4 = (10, 20, 30)
print(t4, type(t4))  # (10, 20, 30) <class 'tuple'>

# Task 2:  Tuple is Safe and List is Unsafe
# List is Unsafe
l1 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
l1[0] = "NameOne"
print(l1)  # ['NameOne', 20, 30, 40, 50]

# Tuple is safe
# t1 = (10, 20, 30, 40, 50)
#      0   1   2   3   4
# t1[0] = "NameOne"
# print(t1)  #  TypeError: 'tuple' object does not support item assignment

# Task 3: Repetition
t1 = (10, 20, 30, 40, 50)
print(t1 * 2)  # (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
print(t1 * 3)  # (10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
print(t1)  # (10, 20, 30, 40, 50)



