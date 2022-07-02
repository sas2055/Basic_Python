"""
# set:
    - A Set is an unordered collection data type that is iterable.
    - set is mutable data type and background data structure is HASH TABLE.
    - set does not support array, indexing and slicing.
    - it accepts homogeneous / heterogeneous values.
    - it does not preserve sequence order and duplicates are not allowed.
---------------------------------------------------------------------------

# Que. how to declare a set
->    it is a empty set()
----------------------------------------------------------------------------

# Que. how to create a set
->      type({()}), a = set(), set()
---------------------------------------------------------------------------

# set methods:
x = {10, 20, 30, 40}
y = {2, 0, 10, 50, 30}
print('x union y', x&y)
print('x intersection y', x|y)
print('x symmetric difference y', x^y)
print('x difference y', x-y)
-------------------------------------------------------------------------

a = {'red', 'yellow', 'pink', 'white', 'black', 'green'}
b = {'black', 'green', 'blue', 'grey'}
a.add('brown')
print('add element is: ', a)
a.update(b)
print('update element is: ', a)
a.remove('red')
print('remove element is: ', a)
a.discard('pink')
print('remove specified element is: ', a)
print('remove an element is: ', a.pop(), ': and list is: ', a)
print('the list is: ', a)
print('the list is: ', b)
print('uncommon element of set 1 is: ', a.difference(b))
print('common element quit of set is: ', a.symmetric_difference(b))
print('return a set is: ', a.union(b))
print('common element of set is: ', a.intersection(b))
print('clear the set is: ', a.clear())
print(a)
--------------------------------------------------------------------

p = {1, 2, 3, 4, 5, 8, 9}
q = {3, 4, 5, 8}
print('p intersection q', p.isdisjoint(q))
print('p contain not q is: ', p.issubset(q))
print('q contain p is: ', q.issubset(p))
print('p contain q is: ', p.issuperset(q))
=========================================================================
"""

