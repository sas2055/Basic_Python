"""
# bytes():
    - it is used to generate byte sequence for given list of int
    - it is return byte object
    - it has a range: 0 - 256 (ASCII characters)
    - it is immutable because it does not contain any mutable method
    - bytes does not support item assignment of value
-------------------------------------------------------------
syntax:
    bytes(source, encoding, errors)
----------------------------------------------------------

Parameter Value:
       1. source:
            It is used to initialise the bytes array.
       2. encoding:
            It is used for encoding of string.
       3. errors:
            It is used to specify what to do if the encoding fails.
----------------------------------------------------------------
print(bytes(2))
print(bytes(4))
-------------------------------------------------------------

k = [12, 4, 60]
print(bytes(k))
--------------------------------------------------------------

k = [12,4,60]
bt = bytes(k)
print(bt[-1])
# bt[-1] = 30
# in case of bytes direct assignment of value is nt possible
print(dir(bt))
# as it does nt contain any mutable method hence bytes is immutable
-----------------------------------------------------------------

# convert string to bytes
message = 'Python is fun'
byte_message = bytes(message, 'utf-8')
print(byte_message)
-------------------------------------------------------------------

# string with encoding 'utf-8'
string = 'Python is interesting.'
array = bytes(string, 'utf-8')
print(array)
------------------------------------------------------------------

# Array of bytes of given integer size
s = 5
print(bytes(s))
------------------------------------------------------------------

# Array of bytes from an iterable list
ls = [1, 2, 3, 4, 5]
print(bytes(ls))
=================================================================

# bytearray():
       - it is same as that of bytes but bytearray is Mutable in nature
       - it is returns a bytearray object which is an array of given bytes.
       - it contains methods those support mutable operations, and changes
        persist in the same object hence its mutable
       - it has a range: 0 - 256 (ASCII characters)
       - it is support item assignment
-----------------------------------------------------------------------
Syntax:
        bytearray(source, encoding, errors)
----------------------------------------------------------------------

k = [12, 4, 60]
bt = bytearray(k)
print(bt)
print(bt[-1])
bt[-1] = 30
print(bt)
print(bt[-1])
print(dir(bt))
-------------------------------------------------------------------

# convert list to bytearray
prime_numbers = [2, 3, 5, 7]
byte_array = bytearray(prime_numbers)
print(byte_array)
-------------------------------------------------------------------

# string with encoding 'utf-8'
string = 'Python is interesting.'
array = bytearray(string, 'utf-8')
print(array)
------------------------------------------------------------------

# Array of bytes of given integer size
s = 5
print(bytearray(s))
------------------------------------------------------------------

# Array of bytes from an iterable list
ls = [1, 2, 3, 4, 5]
print(bytearray(ls))
====================================================================
"""
