#Iterable in Python
#String, list, tuple is an iterable item in Python
#So, you could use string, or list, or tuple for _iterable variable's value

#Set is unordered and unique value (duplicate value is not allowed)

# _iterable   =   "Falentino"
# _iterable   =   [1, 2, 3, 1, 5, 7, 1, 2, 8, 9]
_iterable   =   ('apple', 'banana', 'cherry', 'chocolate', 'cherry')

_mySet  =   set(_iterable)
_string =   input('What you are looking for?\n')

if _string in _mySet:
    print(f'{_string} in that set')
    print(_mySet)
else:
    print('Item is not there')