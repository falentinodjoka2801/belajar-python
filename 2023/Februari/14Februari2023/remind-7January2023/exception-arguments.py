#We can get or set some arguments in an exception. If you want to get exception's argument, just call "args" property in your exception object variable (instantiation)
#and it will return a tuple contains its arguments.
#If you wannna set some arguments in an exception, just include those as argument in exception constructor.

#Set some arguments
try:
    raise Exception('January', 'March', 'May')
except Exception as e:
    for argument in e.args:
        print(argument)