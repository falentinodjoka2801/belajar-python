def mid(string):
    lenOfString     =   len(string)
    isLenEven       =   lenOfString % 2 != 0

    returnedCharacter   =   ''

    if isLenEven:
        middleIndex         =   (lenOfString + 1) / 2
        middleIndex         =   int(middleIndex) - 1
        returnedCharacter   =   string[middleIndex]

    return returnedCharacter

try:
    while True:
        enteredString   =   input('Enter a string : ')
        if len(enteredString) >= 1:
            break

    middleCharacter =   mid(enteredString)
    print(middleCharacter)
except KeyboardInterrupt:
    print('\nYou close the running program')