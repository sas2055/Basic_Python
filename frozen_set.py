"""
# frozen set:
    - it is returns an immutable object initialized with elements from the given iterable.
    - Frozen set is just an immutable version of a Python set object.
    - While elements of a set can be modified at any time,
    elements of the frozen set remain the same after creation.
    - frozen sets can be used as keys in Dictionary or as elements of another set.
    - it is does not contain mutable methods.
    ex - pop, remove, update, add, discard
--------------------------------------------------------------------------------
syntax:
    frozenset([iterable])
--------------------------------------------------------------------------------

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print('The frozen set is: ', frozenset(vowels))
print('The empty frozen set is: ', frozenset())
--------------------------------------------------------------------

# random dictionary
person = {'name': 'suraj', 'age': 20, 'sex': 'male'}
frozenset(person)
print('The frozen set is: ', frozenset(person))
--------------------------------------------------------------------------

# list to set conversion
my_list = ['apple', 'banana', 'cherry']
x = frozenset(my_list)
print(x)
------------------------------------------------------------------------

# frozenset operations:
        - Like normal sets, frozenset can also perform different operations
---------------------------------------------------------------------------

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)

# union
print(A.union(B))

# intersection
print(A.intersection(B))

# difference
print(A.difference(B))

# symmetric_difference
print(A.symmetric_difference(B))
=========================================================================
"""