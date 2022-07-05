"""
# tuple:
    - it is a collection of elements separated by commas.
    - it is an ordered and unchangeable collection of data objects.
    - it is immutable data type and background data structure is array.
    - its support indexing and slicing.
    - it is not support item assignment
    - it accepts homogeneous / heterogeneous values.
    - it preserves sequence order and duplicates are allowed.
    - it is not used to performing manipulation
-------------------------------------------------------------------------

# Que. how to declare a tuple
->  ()    (round bracket)
----------------------------------------------------------------------

# Que. how to create a tuple
->      (), tuple(), a = (), type(())
-------------------------------------------------------------------

# tuples methods:
    it has only 2 methods : 1. index and 2. count
---------------------------------------------------------------------

# count the numbers
t = (10, 20, 30, 40, 50, 50, 10, 10)
print('count of 10 is: ', t.count(10))
print('count of 50 is: ', t.count(50))
--------------------------------------------------------------

# proper indexing the numbers
t = (10, 20, 30, 40, 50, 50, 10, 10)
print('index of 10 is: ', t.index(10))
print('index of 50 is: ', t.index(50))
--------------------------------------------------------------------

# negative indexing
t = (1, 2, 3, 4)
print('negative indexing is: ', t[-1])
print('negative indexing is: ', t[-3])
---------------------------------------------------------------------------

# positive indexing
t = (1, 2, 3, 4)
print('positive indexing is: ', t[1])
print('positive indexing is: ', t[3])
---------------------------------------------------------------------------

# slicing using reverse
t = (1, 2, 3, 4)
print('reverse the tuple: ', t[::-1])
print('reverse the tuple: ', t[2:])
print('reverse the tuple: ', t[2::-1])
------------------------------------------------------------------

t1 = (1, 2, 3, 4)
print('t1 is: ', t1)
print('t1 id is: ', id(t1))
t2 = (5, 6, 7, 8)
print('t2 is: ', t2)
print('t2 id is: ', id(t2))
t1 = t1 + t2
print('t1 after concatenation is: ', t1)
print('t1 id after concatenation is: ', id(t1))
t3 = t1
print('t3 id is: ', id(t3))
# t1 and t2 are not changed
# t1, t2, t3 ids are not same and not a change perform then it is immutable data type
# t1 id is:  1846846159456
# t2 id is:  1846850783568
# t3 id is:  1846846494800
===========================================================================

# packing:
     - grouping multiple objects in a single identifier
-------------------------------------------------------------------

a = 10, 20, 30
print('integer number is: ', a)
---------------------------------------------------------------
film = 'k', 'g', 'f'
print('film is: ', film)
---------------------------------------------------------
f = 2.3, 5.7, 5.8
print('floating number is: ', f)
=======================================================================

# unpacking:
       - to unfold packed values, we need multiple identifier
----------------------------------------------------------------------

a, b, c = 10, 20, 30
print('1st in number is: ', a)
print('2nd int number is: ', b)
print('3rd int number is: ', c)
------------------------------------------------------------------------

film = ('k', 'g', 'f')
x, y, z = film
print(x)
print(y)
print(z)
------------------------------------------------------------------------

f, g, h = 2.3, 5.7, 5.8
print('1st float number is: ', f)
print('2nd float number is: ', g)
print('3rd float number is: ', h)
==========================================================================

# Que. list are taken more memory than tuple
# check size of tuple of t1
t1 = (1, 2, 3, 4)
print(t1.__sizeof__())

# check size of list of l1
l1 = [1, 2, 3, 4]
print(l1.__sizeof__())
========================================================================
"""