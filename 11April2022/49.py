#*args
# def _sayHelloLastNight(*peopleThatSaidHelloLastNight):
#     print(peopleThatSaidHelloLastNight)
#     for _people in peopleThatSaidHelloLastNight:
#         print('{} said "Hello" to you last night'.format(_people))

# _sayHelloLastNight('Falentino', 'Andrian', 'Tino', 'Hendra', 'Agus')

#**kwargs
# def _sayHello(name, **params):
#     if('day' in params):
#         print('Hello {}, good {}'.format(name, params['day']))
#     else:
#         print('Hello brother, {}!'.format(name))

# _sayHello('Falentino', day='Morning')

def myfunc(*numbers):
    _list   =   list()
    for i in numbers:
        _list.append(i)
        
    return _list

print(myfunc(1, 5, 9, 3, 7))