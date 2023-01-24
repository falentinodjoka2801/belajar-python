def thousandSeparator(number):
    stringNumber: str   =   str(number)

    reversedStringNumber    =   ''
    for indexData, character in enumerate(reversed(stringNumber)):
        item    =   character
        if indexData >= 3:
            if indexData % 3 == 0:
                item    =   f',{character}'

        reversedStringNumber    +=  item

    formattedNumber     =   reversedStringNumber[::-1]
    return formattedNumber

formattedNumber     =   thousandSeparator(10000000000)
print(formattedNumber)