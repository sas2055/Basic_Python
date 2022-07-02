"""
# typecasting / data conversion:
        The process of converting the value of one data type (integer, string, float, etc.)
    to another data type is called type conversion.
    Python has two types of type conversion.
---------------------------------------------------------------------------

# 1. implicit typecasting:
        In Implicit type conversion, Python automatically converts one data type to another data type.
    This process doesn't need any user involvement.
------------------------------------------------------------------------

print(10/5)
print('10'+'20')
print('data science is most important')
print(4*6)
print(0b11111)
print(4 + 7j)
-------------------------------------------------------------------------

# Que.1 converting integer to float
num_int = 10
num_flo = 12.4
num_new = num_int + num_flo
print('data type of num_int: ', type(num_int))
print('data type of num_flo: ', type(num_flo))
print('value of num_new: ', num_new)
print('data type of num_new: ', type(num_new))
===================================================================

# Que. 2 addition of string and integer
num_int = 100
num_str = '234'
print('data type of num_int: ', type(num_int))
print('data type of num_str: ', type(num_str))
print(num_int + num_str)
===============================================================

# 2. explicit type casting:
        In Explicit Type Conversion, users convert the data type of an object to required data type.
    We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
------------------------------------------------------------------------------

print(int(10/5))
print(hex(0b11111))
print(list(range(1,11)))
print(int('10')+int('40'))
print(dict.fromkeys('Shiljit', 'Name'))
-----------------------------------------------------------------------

# Que.3 addition of string and integer
num_int = 12
num_str = '123'
print('data types of num_int: ', type(num_int))
print('data types of num_str before type casting: ', type(num_str))
num_str = int(num_str)
print('data types of num_str after type casting: ', type(num_str))
num_sum = num_int + num_str
print('sum of num_int and num_str: ', num_sum)
print('data type of  the sum: ', type(num_sum))
===================================================================
"""
