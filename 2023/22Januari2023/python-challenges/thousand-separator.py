def format_number(number: int):
    stringNumber: str       =   str(number)
    reversedStringNumber    =   reversed(stringNumber)
    
    reversedString  =   ''
    reversedNewStringList: list   =   []
    for indexData, reversedItem in enumerate(reversedStringNumber):
        item        =   reversedItem
        itemString  =   reversedItem
        if(indexData >= 3):
            if indexData % 3 == 0:
                item        =   f'{reversedItem},'
                itemString  =   f',{reversedItem}'
        
        reversedString  +=  itemString
        reversedNewStringList.append(item)

    # reversedNewStringList.reverse()

    print(reversedString)
    print(reversedNewStringList)

    newReversedString  =   reversedString[::-1]
    reversedNewStringList.reverse()

    print(newReversedString)
    print(reversedNewStringList)
    
    # reversedString  =   ''
    # for character in reversedNewStringList:
    #     reversedString  +=  character

    newReversedString  =   reversedString[::-1]
    return newReversedString


formattedNumber     =   format_number(1000000000)
# print(formattedNumber)

# name    =   input('What is your name? ')
# print(f'Original name : {name}')
# print(f'Reversed name : {name[::-1]}')