def double_letters(string):
    for index, character in enumerate(string):
        nextIndex       =   index + 1
        nextCharacter   =   string[nextIndex]

        doubleLetterCount =   0
        if character == nextCharacter:
            doubleLetterCount   +=  1
            break

    thereIsDoubleLetter     =   doubleLetterCount >= 1
    return thereIsDoubleLetter

print(double_letters('whatthefuck'))
        