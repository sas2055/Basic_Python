"""
print('hello')
print('hello good morning')
print('hello good evening every body')
==========================================================
# identifier:
        An identifier is a name given to entities like class, functions, variables, etc.
    It helps to differentiate one entity from another.
-------------------------------------------------------------------

# identifier rule
    1. identifier can be a combination of letter in lower case (a-z), upper case (A-Z), digits (0-9)
        an underscore _.
    2. an identifier cannot start with a number.
    3. we can use alphabets + numbers.
    4. special symbols and characters are not allowed.
    5. between 2 characters or word space is not allowed.
    6. keyword cannot be use an identifiers.
    7. an identifier can be of any length.
------------------------------------------------------------------

# a is an identifier
a = 100
print(a)
print(id(a))
b = 'python'
print(b)
print(id(b))
--------------------------------------------------------------

# A and a makes a different here then python is case-sensitive language.
A = 'java'
print(A)
print(id(A))
-----------------------------------------------------------------

# numbers are suffix is allowed
a5 = 'good morning'
print(a5)
-------------------------------------------------------------------

# _ underscore is allowed
bank_name = 'SBI'
print(bank_name)
----------------------------------------------------------------

# we can use special characters in our identifiers
bank_ifsc = 'SBI@$@1234'
print(bank_ifsc)
=====================================================================

# keyword:
      - Keywords are the reserved words in Python.
      - We cannot use a keyword as a variable name, function name or any other identifier.
      - They are used to define the syntax and structure of the Python language.
      - In Python, keywords are case-sensitive.
      - There are 35 keywords in Python 3.10.4
======================================================================

# Que.1 how to check object exists into the memory
->    use id() function of a python
====================================================================

# Que.2 how to check keyword present in python
->  we have to import keyword libraly
  import keyword
  print(keyword.kwlist)
================================================================

# Que.3 how to count total number of keyword present in python
->   use len() function
==================================================================

# Que.4 how to understand meaning of each keyword
->    use help() function
==================================================================

# \n for a new line
print('hello \ngood morning \nto all participants')
# \t for a tab
print('hello \tgood morning \tto all participants')
# space is also considered as a block
print('          hello          ')
-----------------------------------------------------------------

name = 'shital ajit shelar'
age = 27
weight = 45
print('my name is: ',name)
print('age is: ', age, 'weight is: ', weight)
print('my name is: ',name, 'age is: ', age, 'weight is: ', weight)
print('my name is: {}, age is: {}, and weight is: {}'.format(name,age,weight))
print('my name is: {2}, age is: {0}, and weight is: {1}'.format(age,weight,name))
print('my name is: %s, age is: %d, and weight is: %d'%(name,age,weight))
print('my name is: %s, age is: %f, and weight is: %f'%(name,age,weight))
---------------------------------------------------------------------------------

n1 = 'sanika'
n2 = 'akshara'
n3 = 'shivansh'
print('we have 3 friends: %s, %s, %s'% (n1,n2,n3))
print('we have 3 friends: %s, %s, %s'% (n2,n3,n1))
print('we have 3 friends: %s, %s, %s'% (n3,n1,n2))
==================================================================
"""