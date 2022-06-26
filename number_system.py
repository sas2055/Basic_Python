"""
# number system:
         Number System is a system that defines numbers in
    different ways to represent numbers in different forms.
------------------------------------------------------------------

Types of Number System:
        The number system in python is represented using the following four systems:

1. Binary Number System:
       - A number system with base or radix 2 is known as a binary number system.
       - Only 0 and 1 are used to represent numbers in this system.
-----------------------------------------------------------------------

n = 120
print(type(n))
print('binary to decimal: ', 0b1111000)
print('binary to octal: ', oct(0b1111000))
print('binary to hexadecimal: ', hex(0b1111000))
=======================================================================

2. Octal Number System:
      - Octal Number System is one in which the base value is 8.
      - It uses 8 digits i.e. 0-7 for the creation of Octal Numbers.
      - It is also a positional system that is weight is assigned to each position.
------------------------------------------------------------------------

n = 120
print(type(n))
print('octal to decimal: ', 0o170)
print('octal to hexadecimal: ', hex(0o170))
print('octal to binary: ', bin(0o170))
===================================================================

3. Decimal Number System:
       - A number system with a base value of 10 is termed a Decimal number system.
       - and it is represented using digits between (0 to 9).
------------------------------------------------------------------------------

 n = 120
print(type(n))
print('decimal to binary: ', bin(n))
print('decimal to octal: ', oct(n))
print('decimal to hexadecimal: ', hex(n))
==============================================================================

4. Hexadecimal Number System:
         - A number system with a base of 16 is called a hexadecimal number system.
         - It is represented using numbers between use 0 to 9 and the alphabets between A to F.
         - As both numeric digits and alphabets are used in this system,
         - it is also called an alphanumeric system.
---------------------------------------------------------------------------

n = 120
print(type(n))
print('hexadecimal to decimal: ', 0x78)
print('hexadecimal to binary: ', bin(0x78))
print('hexadecimal to octal: ', oct(0x78))
============================================================================
"""