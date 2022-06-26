"""
# operators in python:
        used to perform some operations on variables and values.
---------------------------------------------------------------------------------

# 1. arithmetic operators:
        arithmetic operators are used with numeric values to perform common mathematical operations.

 operator       name               example          description
    +         addition              x + y        adds two operands
    -         subtraction           x - y        minus two operands
    *         multiplication        x * y        it multiplies two operands
    /         division              x / y        it divides two operands
    %         mod                   x % y        its  divide two operands and returns remainder
    **        exponent              x ** y       left operand is raised to the power of right
    //        floar division        x // y       division that results into whole number
---------------------------------------------------------------------------------

a = 10
b = 20
print('addition is:', a+b)
print('subtraction is:', a-b)
print('multiplication is:', a*b)
print('division is:', a/b)
----------------------------------------------------------------

x = 50
y = 20
print('x + y = ', x+y)
print('x - y = ', x-y)
print('x * y = ', x*y)
print('x / y = ', x/y)
z = 2
print('x ** z = ', x**z)
print('x // y = ', x//y)
=============================================================

# 2. assignment operators:
        assignment operators are used to assign values to variable

 operator       example        description
    =           x = y         assign value
    +=          x += y        add and operator
    -=          x -= y        minus and operator
    *=          x *= y        multiply and operator
    /=          x /= y        divide and operator
    %=          x %= y        modulus and operator
    **=         x **= y       exponent and operator
    //=         x //= y       floar division
------------------------------------------------------------------

a = 100
print(a)
a = 70 + 30
print('a sign value a = ', 70 +30 )
a += 100    # a = a + 100
print('addition is: ', a)
a -= 50     # a = a - 50
print('substraction is: ', a)
a *= 2      # a = a * 2
print('multiplication is: ', a)
a /= 10     # a = a / 10
print('division is: ', a)
a **= 2     # a = a ** 2
print('exponent is: ', a)
a //= 10      # a = a // 10
print('floar division is: ', a)
a %= 2      # a = a % 2
print('reminder is: ', a)
===================================================================

# 3. relational/ conditional operators:
        relation operators are used to compare two values and result is always boolean output.

 operator       name                   example
    <         greater than              x < y
    >         less than                 x > y
    <=       greater than equal to      x <= y
    >=       less than equal to         x >= y
    ==         equal to                 x == y
    !=         not equal                x != y
---------------------------------------------------------------------

x = 10
y = 5
print('x < y is: ', x < y)
print('x > y is: ', x > y)
print('x <= y is: ', x <= y)
print('x >= y is: ', x >= y)
print('x != y is: ', x != y)
print('x == y is: ', x == y)
======================================================================

# 4. logical operators:
        logical operators are used to combine conditional statements and output is always boolean output.

 operator       description                 example
    and       returns true if both         x < 5 and
              statements are true           x < 10

    or        returns true if one of        x < 5 or
              the statements is true         x < 4

    not        reverse the result,         not(x < 5 and
               returns false if the         x < 10)
                result is true
----------------------------------------------------------------
# and operator:
name = 'shital'
age = 27
print(name == 'shital' and age == 27)
print(name == 'shivansh' and age == 27)
print(name == 'shital' and age == 20)
print(name == 'shiv' and age == 3)
--------------------------------------------------------------------------

# or operator:
name = 'shital'
age = 27
print(name == 'shital' or age == 27)
print(name == 'shivansh' or age == 27)
print(name == 'shital' or age == 20)
print(name == 'shiv' or age == 3)
-------------------------------------------------------------------------

# not operator:
name = 'shital'
age = 27
print(not(name == 'shivansh'))
print(not(name == 'shital'))
print(not(age == 27))
print(not(age == 25))
----------------------------------------------------------------

# value of true is 1
# value of false is 0
# x and y:
        -if ur x is true then return y
        - false means 0, none, ''
        - if ur x is false then return x
----------------------------------------------------------------------

print('shiv' and 'ajit')
print('False' and 12)
print('None' and 'jaya')
print(0 and 78)
========================================================================

# 5. identity operators:
        identity operators are used to compare the objects, its check id / address of an objects.
    if address matches then it results true otherwise false.

 operator       description                         example
    is       returns true if both                  x is y
            variables are the same object

  is not      returns true if both variables       x is not y
                are not the same object
--------------------------------------------------------------------------

x = ['red', 'yellow', 'green']
y = ['red', 'yellow', 'green']
z = x
print('x is z: ', x is z)
print('x is y: ', x is y)
print('x == y: ', x == y)
print('x is not z: ', x is not z)
print('x is not y: ', x is not y)
print('x != y: ', x != y)
----------------------------------------------------------------------

x = 20
y = 20
z = x
print('x is z: ', x is z)
print('x is y: ', x is y)
print('x == y: ', x == y)
print('x is not z: ', x is not z)
print('x is not y: ', x is not y)
print('x != y: ', x != y)
============================================================================

# 6. membership operators:
        membership operators are used to should be checks either an element is a member of a
    sequence or not in an objects, it returns boolean output.

 operator               description                           example
    in       returns true if a sequence with the              x in y
            specified value is present in the object

  not in      returns true if a sequence with the            x not in y
            specified value is not present in the object
------------------------------------------------------------------------------

x = 'sonali kulkarni'
print('sonali' in 'sonali kulkarni')
print('sonali bendre' in 'sonali kulkarni')
print('sonam' not in 'sonali kulkarni')
print('sonali bendre' not in 'sonali kulkarni')
---------------------------------------------------------

a = [12, 34, 45, 10, 20]
b = 45
print(b in a)
print(b not in a)
=========================================================================

# 7. bitwise operators:
        bitwise operators are used to compare binary numbers.

operator     name            description
  &          and        sets each bit to 1 if both bits are 1

  |          or         sets each bit to 1 if one of two bits is 1

  ^          xor        sets each bit to 1 if only one of two bits is 1

  ~          not            inverts all the bits

  <<       zero fill      shift left by pushing zeros in from
           left shift     the right and let the leftmost bits fall off

  >>       signed right   it right shifts by pushing copies of the leftmost bit in
            shift          form the left and let the rightmost bits fall off
----------------------------------------------------------------------------------

x = {10, 20, 30, 40}
y = {2, 0, 10, 50, 30}
print('x and y is: ', x&y)
print('x or y is: ', x|y)
print('x xor y is: ', x^y)
---------------------------------------------------------

z = 20
a = 10
print('~z is: ', ~z)
print('zero fill left shift is: ', z << a)
print('signed right shift is: ', z >> a)
=================================================================
"""
