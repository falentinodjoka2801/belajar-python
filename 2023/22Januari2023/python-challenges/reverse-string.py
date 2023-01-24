name    =   input('Enter your name : ')
reversedNameWithBackwardOperator    =   name[::-1]

reversedNameWithList    =   []
for character in name:
    reversedNameWithList.append(character)

reversedNameWithList.reverse()

print(reversedNameWithBackwardOperator)
print(reversedNameWithList)