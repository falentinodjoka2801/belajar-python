def capital_indexes(string):
    uppercaseIndexes    =   []
    for index, character in enumerate(string):
        if character.isupper():
            uppercaseIndexes.append(index)
    
    return uppercaseIndexes

capitalIndexes  =   capital_indexes('HeLlO')
print(capitalIndexes)
