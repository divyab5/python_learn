# what are datatypes in python
# numbers: int, float, bool, complex
product_id = 4567
print(product_id, type(product_id))  # 4567 <class 'int'>
product_price = 50000.00
print(product_price, type(product_price))  # 50000.0 <class 'float'>
product_available = True
print(product_available, type(product_available))  # True <class 'bool'>

# strings : str
product_name = "Dell"
print(product_name, type(product_name))  # Dell <class 'str'>

# sequences:
# list(order, unsafe),
# tuple(order, safe)
# set(un order, unsafe)
# frozenset(safe)
# bytes, bytearray, (files)
# range (iterations)
product_items = ['item1', 'item2', 'item3', 'item4']
print(product_items, type(product_items))  # ['item1', 'item2', 'item3', 'item4'] <class 'list'>

# mapping
# dict
# {key: value}
d = {'details': 'details'}

# details(presentation layer --- details(middleware layer)

