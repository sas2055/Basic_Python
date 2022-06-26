"""
# dict.:
   - Dictionaries are used to store data values in key:value pairs.
   - A dictionary is a collection which is ordered*, changeable
   - do not allow duplicate keys but duplicate values are allowed.
   - dict. is mutable data type and background data structure is HASH TABLE.
   - dict does not support array, indexing and slicing.
   - it accepts homo./ hetro. values.
   - key plays role of index
----------------------------------------------------------------------------

# Que. how to declare a dict
->      {} (curly bracket)
----------------------------------------------------------------------------

# dict methods:
d = {1:'red',2:'yellow',3:'green',4:'blue',5:'black',6:'white'}
print('dict is: ',d)
print('all keys are: ', d.keys())
print('all values are: ', d.values())
print('all keys and values are: ', d.items())
print('remove pair is: ', d.popitem(),d)
print('remove value is: ', d.pop(5),d)
print('value is: ', d.get(3),d)
t = [1,2,3,4]
print('dictionary of t is: ', dict.fromkeys(t,'num'))
print('clear the dict is: ', d.clear(),d)
======================================================================
"""