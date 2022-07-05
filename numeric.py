"""
# numeric:
    - numeric data type represent the data which has numeric value.
    - Numeric value can be integer, floating number or even complex numbers.
    - These values are defined as int, float, complex and bool class in Python.
-------------------------------------------------------------------------------

1. Integers –
    - This value is represented by int class.
    - It contains positive or negative whole numbers (without fraction or decimal).
    - we don't have a limit for integer value
    - base 10 (0 - 9)
------------------------------------------------------------------------------
syntax:     int(value, base)
-----------------------------------------------------------------------------

a = 5
print('Type of a: ', type(a))
-----------------------------------------------------------------------------

x = int(3.5)
print(x)
-------------------------------------------------------------------------

x = int(10)
print(x)
===============================================================================

2. Float –
    - This value is represented by float class.
    - It is a real number with floating point representation.
    - It is specified by a decimal point.
    - Optionally, the character e or E followed by a positive or negative integer
    may be appended to specify scientific notation.
------------------------------------------------------------------------------
syntax:     float(value)
---------------------------------------------------------------------------

b = 5.0
print('Type of b: ', type(b))
----------------------------------------------------------------------------

x = float(3.5)
print(x)
------------------------------------------------------------------------

x = float(10)
print(x)
=================================================================================

3. Complex Numbers –
    - Complex number is represented by complex class.
    - It is specified as (real part) + (imaginary part)j.
------------------------------------------------------------------------------
syntax:     complex(real, imaginary)
--------------------------------------------------------------------------

c = 2 + 4j
print('Type of c: ', type(c))
--------------------------------------------------------------------------

x = complex(3 + 5j)
print(x)
---------------------------------------------------------------------

x = complex(10)
print(x)
=====================================================================

4. Boolean:
    - Booleans represent True or False values.
-------------------------------------------------------------------

# When you compare two values, the expression is evaluated
it returns the Boolean output
print(10 > 9)
print(10 == 9)
print(10 < 9)
--------------------------------------------------------------------

# if statement
a = 200
b = 33

if b > a:
  print('b is greater than a')
else:
  print('b is not greater than a')
----------------------------------------------------------------

# Evaluate a string and a number:
print(bool('Hello'))
print(bool(15))
-----------------------------------------------------------

# Evaluate two variables:
x = 'Hello'
y = 15

print(bool(x))
print(bool(y))
---------------------------------------------------------

# some values are True
bool('abc')
bool(123)
bool(["apple", "cherry", "banana"])
------------------------------------------------------------

# Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
------------------------------------------------------------

# Functions can Return a Boolean
def my_func():
  return True

print(my_Func())
----------------------------------------------------------

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
================================================================
"""
