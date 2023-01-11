def multiplyByOne(x):
    print(f'do one : {x*1}')
    
def multiplyByTwo(x):
    print(f'do two : {x*2}')

def multiplyByThree(x):
    print(f'do three : {x*3}')

def multiplyByFour(x):
    print(f'do four : {x*4}')

def multiplyByItSelf(x):
    print(f'Multiply by itself {x*x}')

xValue   =   int(input('Input = '))

actionMap   =   {1 : multiplyByOne, 2 : multiplyByTwo, 3 : multiplyByThree, 4 : multiplyByFour}
action      =   actionMap.get(xValue, multiplyByItSelf)

print(type(action))

action(xValue)

#Instead of using an endless if else statement, you could use map concept (or dictionary in python) to contain
#your block of code that contained in a function as a value, and use your condition as a key.
#So, if you have a condition 1 to run trueFunc() and 2 to run falseFunc, you could write {1 : trueFunc, 2 : falseFunc}
#But you need to contain your return value (function) in a variable, that variable type is a function
#You can run that function with that variable's name, don't forget to add parenthesis to notate that variable as a function
#You can add some parameters if necessary