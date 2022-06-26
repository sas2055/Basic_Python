"""
# list:
    - list is an ordered and changeable collection of data objects.
    - list is mutable data type and background data structure is array.
    - its support indexing and slicing.
    - it accepts homo./ hetro. values.
    - it preserves sequence order and duplicates are allowed.
-------------------------------------------------------------------------

# Que. how to declare a list
->  []
-----------------------------------------------------------------

# list methods
l = [1, 2, 3]
print('list is: ', l)
print('add element is: ', l.append('java'), l)
print('remove element is: ', l.pop(),l)
print('add a iterables: ', l.extend('python'), l)
print('reverse the list: ', l.reverse(), l)
print('insert the element: ', l.insert(-1,10), l)
l1 = l.copy()
print('l1 is shallow copy of l: ', l1)
print('empty list is: ', l1.clear(), l1)
print('add a iterables', l1.extend([100,4,30]), l1)
print('increase order is: ', l1.sort(), l1)
print('decrease order is: ', l1.sort(reverse=True), l1)
print('index of 1 is: ', l.index(1))
print('count of 1 is: ', l.count(1))
print('remove element is: ', l.remove('s'), l)
----------------------------------------------------------------------

ls = [12, 34, 25, 67, 13, 69, 28]
print('list is: ', ls)
print('minimum value is: ', min(ls))
print('maximum value is: ', max(ls))
print('sum of all elements is: ', sum(ls))
print('increase order is: ', ls.sort(), ls)
print('decrease order is: ', ls.sort(reverse=True), ls)
=========================================================================
"""