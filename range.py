"""
# range:
     - The range() is an in-built function in Python.
     - The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default), and stops before a specified number.
    - range(n/stop) => stop is exclusive, stop will not be added in the output.
    - it will generate 0 - n
    - range(start, stop, step)
---------------------------------------------------------------------

# Que.1 generates 1-100 numbers
print(list(range(1, 101)))
print(tuple(range(101, 1, -1))) # negative stepping of -1
print(set(range(1, 101)))
=====================================================

# Que.2 generates 1-100 even numbers
print(list(range(2, 101, 2)))
print(tuple(range(100, 2, -2))) # negative stepping of -2
print(set(range(2, 101, 2)))
==========================================================

# Que.3 generates 1-100 odd numbers
print(list(range(1, 101, 2)))
print(tuple(range(1, 101, 2)))
print(set(range(1, 101, 2)))
========================================================
"""
