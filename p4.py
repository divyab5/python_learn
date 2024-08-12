# Data-Structure: Array
# list : unsafe (mutable), ordered, duplicates allowed
# tuple : safe (immutable), ordered, duplicates allowed

# Data-Structure: HashTable
# set: unsafe (mutable), un-ordered, no duplicates allowed
# frozenset :  safe (immutable), un-ordered, no duplicates allowed

# dict:
# We can create dict using ```{}``` and object ```dict()```
# In dict we can store key value information
# In dict values can be duplicated
# In dict key cannot be duplicate

# Theory:
# we can create set using ```set()``` object and user curly braces with minium 1 value ```{10}```
# Task 1: Set is un-ordered
s1 = {10, 20, 30, 40, 50}
print(s1)  # {50, 20, 40, 10, 30}

# Task 2: Set duplicates not allowed
s1 = {10, 20, 30, 40, 50, 10, 30, 60, 70, 80}
print(s1)  # {70, 40, 10, 80, 50, 20, 60, 30}

# In set there is no slicing and indexing
# print(s1[0])  # TypeError: 'set' object is not subscriptable

# Task 3: create dict
d1 = {1: 20, 2: 30, 3: "NameOne", 4: "NameTwo"}
print(d1)
d2 = dict({1: 20, 2: 30, 3: "NameOne", 4: "NameTwo"})
print(d2)

d2[1] = "Sai Kiran"
print(d2)


