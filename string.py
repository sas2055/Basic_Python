"""
# string:
    - it is global data type because it accepts everything
    - string is immutable data type and background data structure is array.
    - its support indexing and slicing.
    - slicing always start from 0
    - [start: stop: step]
---------------------------------------------------------------------
# Que. how to declare a string
->  ' ' or " "
---------------------------------------------------------------------

# string methods
s = 'data scientist'
print(s)
print('reverse the string:', s[::-1])
print('reverse the scientist is:', s[:3:-1])
print('reverse the data is:', s[-11::-1])
print('reverse the data is:', s[:4][::-1])
print('reverse the tist is:', s[-1:-5:-1])
print('reverse the scien is:', s[9:4:-1])
-----------------------------------------------------------------

s = 'data scientist'
print(s)
print('count of t is:', s.count('t'))
print('count of a is:', s.count('a'))
print('center of the string:', s.center(40))
----------------------------------------------------------------

s = 'data scientist'
print(s)
print('first character of the string is capitalize:', s.capitalize())
print('first character of all the word is capitalized:', s.title())
--------------------------------------------------------------------

s = 'data scientist'
print(s)
print('position of the t is:', s.index('t'))
print('higher position of the t is:', s.rindex('t'))
print('position of the t is:', s.index('m'))
--------------------------------------------------------------------------

s = 'data scientist'
print(s)
print('string startswith:', s.startswith('d'))
print('string startswith:', s.startswith('Data'))
print('string endswith:', s.endswith('t'))
print('string endswith:', s.endswith('s'))
--------------------------------------------------------------------------

s = 'data scientist'
print(s)
print('position of the t is:', s.find('t'))
print('higher position of the t is:', s.rfind('t'))
print('position of the t is:', s.find('m'))
===========================================================================

s = 'pYthOniSt'
print(s.capitalize())
print(s.casefold())
print(s.isalpha())
print(s.upper())
print(s.swapcase())
print(s.lower())
print('access of "t": ', s.count('t'))
============================================================================

p = '1234589'
print(p.isnumeric())
print(p.isdigit())
print(p.isdecimal())
print(p.isdigit())
print(p.isascii())
======================================================================

# translate:
my_dict = {83:  80}
txt = 'Hello Sam'
print(txt.translate(my_dict))
---------------------------------------------------------------------------

# maketrans:
txt = 'Hello Sam'
my_table = txt.maketrans('S', 'P')
print(txt.translate(my_table))
==================================================================================
"""