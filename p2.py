# default value of data types
# when we pass datatype it return its type
print(int)  # <class 'int'>
print(int())  # 0
print(float)  # <class 'float'>
print(float())  # 0.0
print(bool)  # <class 'bool'>
print(bool())  # False
print(str) # <class 'str'>
print(str()) # empty space

# int is a datatype --> it return the class --> If we are having class then we can create object
# eg:
# a = 10, (type: class int) (obj : int())
# b = 10.0 (type: class float) (obj : float())

# Note : for set and dict we use curly braces when we pass data
s1 = {10, 20, 30, 40, 50}

d1 = {1:10, 2:20, 3:30, 4:40, 5:50}

a = 10j
print(a, type(a))
