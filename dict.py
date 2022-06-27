"""
# dict.:
   - Dictionaries are used to store data values in key:value pairs.
   - A dictionary is a collection which is ordered*, changeable
   - do not allow duplicate keys but duplicate values are allowed.
   - dict. is mutable data type and background data structure is HASH TABLE.
   - dict does not support array, indexing and slicing.
   - it accepts homogeneous / heterogeneous values.
   - key plays role of index
----------------------------------------------------------------------------

# Que. how to declare a dict
->      {} (curly bracket)
----------------------------------------------------------------------------

# dict methods:
d = {1: 'red', 2: 'yellow', 3: 'green', 4: 'blue', 5: 'black', 6: 'white'}
print('dict is: ', d)
print('all keys are: ', d.keys())
print('all values are: ', d.values())
print('all keys and values are: ', d.items())
print('remove pair is: ', d.popitem(), d)
print('remove value is: ', d.pop(5), d)
print('value is: ', d.get(3), d)
print('clear the dict is: ', d.clear(), d)
--------------------------------------------------------------------

t = [1, 2, 3, 4]
print('dictionary of t is: ', dict.fromkeys(t, 'num'))
s = [10, 20]
print('dictionary of t is: ', dict.fromkeys(t, s))
----------------------------------------------------------------------

d = {1: 'red', 2: 'yellow', 3: 'green', 4: 'blue', 5: 'black', 6: 'white'}
print('insert key and value is: ', d.setdefault(7, 'green'))
print('the dict is: ', d)
print('specified value of key is: ', d.setdefault(7))
print('specified value of key is: ', d.setdefault(4))
-----------------------------------------------------------------------

# zip() return value:
    - the zip() function returns an iterator of tuple based on the iterable objects.
    - if you do not pass any parameter, zip() return an empty iterator
    - if a single iterable is passed, zip() returns an iterator of
    tuples with each tuple having only one element.
    - if a multiple iterable are passed, zip() returns an iterator of
    tuples with each tuple having element from all the iterables
-------------------------------------------------------------------------------

a = [1, 2, 4, 6, 7]
b = ['A', 'D', 'E', 'T']
print(list(zip(a, b)))
print(dict(zip(a, b)))
print(set(zip(a, b)))
print(tuple(zip(a, b)))
======================================================================
"""