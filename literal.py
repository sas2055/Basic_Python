"""
# literal:
    - it is defined as the raw data assigned to variables
    or constant while programming.
    - literals are a fixed value in source code.
    - it is a short and easily visible way to write a value
----------------------------------------------------------------------

Python has different types of literals.
    - string literals,
    - numeric literals,
    - boolean literals,
    - literal collections,
    - special literal None.
=====================================================================

1. string literals:
    - it can be created by a group(sequence) of Characters
    surrounded by the single(”), double(“”), or triple quotes.
-------------------------------------------------------------------
Examples:

# in single quote
s = 'Python'
print(s)
---------------------------------------------

# in double quote
t = "Data Scientist"
print(t)
------------------------------------------------

# in triple quote (multi-line String)
r = '''suppose we have string
       then it will be created
       by group of character'''
print(r)
=========================================================

# Character literal:
    - It is also a type of string literals where a single
    character surrounded by single or double-quotes.
-----------------------------------------------------------
# character literal in single quote
v = 'n'
print(v)

# character literal in double quotes
w = "a"
print(w)
================================================================

2. Numeric literals:
    - They are immutable and there are three types of numeric literal:
    1. Integer
    2. Float
    3. Complex.
------------------------------------------------------------------

1. Integer literal :
    - Both positive and negative numbers including 0.
    - There should not be any fractional part.
-------------------------------------------------------------------

# integer literal
p = 45
print(p)
--------------------------------------------------------------

# Binary Literals
a = 0b10100
print(a)
--------------------------------------------------------------

# Decimal Literal
b = 50
print(b)
----------------------------------------------------------------

# Octal Literal
c = 0o320
print(c)
--------------------------------------------------------------------

# Hexadecimal Literal
d = 0x12b
print(d)
===================================================================

2. Float literal:
    - These are real numbers having both integer and fractional parts.
------------------------------------------------------------------
# Float Literal
e = 24.8
print(e)
----------------------------------------------------
f = 45.0
print(f)
=================================================================

3. Complex Literal:
    - The numbers will be in the form of the real part and imaginary part.
------------------------------------------------------------------
z = 7 + 5j
print(z)
===================================================================

3. Boolean literals:
    - There are only two Boolean literals in Python.
    - They are true and false.
    - True represents the value as 1 and False represents the value as 0
--------------------------------------------------------------------

a = (1 == True)
print('a is: ', a)
---------------------------------------------------
b = (1 == False)
print('b is: ', b)
--------------------------------------------------
c = True + 3
print('c: ', c)
--------------------------------------------------
d = False + 7
print('d: ', d)
===================================================

4. Literal Collections:
    - There are four different types of literal collections
    1. List literals
    2. Tuple literals
    3. Dict literals
    4. Set literals
---------------------------------------------------------

1. List literals:
    - List contains items of different data types.
    - The values stored in List are separated by comma (,)
    and enclosed within square brackets([]).
    - We can store different types of data in a List.
    - Lists are mutable.
--------------------------------------------------------------

# List literals
number = [1, 2, 3, 4, 5]
print(number)
----------------------------------------------------------------
name = ['Amit', 90, 'anushka', 2]
print(name)
====================================================================

2. Tuple literals:
    - A tuple is a collection of different data-type.
    - It is enclosed by the parentheses ‘()‘ and
    each element is separated by the comma(,).
    - It is immutable.
----------------------------------------------------------------------

# Tuple literals
even_number = (2, 4, 6, 8)
print(even_number)
-----------------------------------------------------------
odd_number = (1, 3, 5, 7)
print(odd_number)
========================================================================

3. Dictionary literals
    - Dictionary stores the data in the key-value pair.
    - It is enclosed by curly-brackets ‘{}‘ and
    each pair is separated by the commas(,).
    - We can store different types of data in a dictionary.
    - Dictionaries are mutable.
---------------------------------------------------------------------

# Dict literals
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
print(alphabets)
------------------------------------------------------------------
information = {'name': 'amit', 'age': 20, 'ID': 20}
print(information)
======================================================================

4. Set literals:
    - Set is the collection of the unordered data set.
    - It is enclosed by the {} and each element is separated by the comma(,).
    - Set is mutable.
-----------------------------------------------------------------------

# Set literals
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
-----------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}
print(fruits)
===========================================================================

5. Special literals:
    - Python contains one special literal (None).
    - ‘None’ is used to define a null variable.
    - If ‘None’ is compared with anything else other than a ‘None’, it will return false.
--------------------------------------------------------------------------

# Special literals
water_remain = None
print(water_remain)
=================================================================================
"""
