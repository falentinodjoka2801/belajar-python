#Write a function named capital_indexes. The function takes a single parameter
#which is a string. Your function should return a list of all the indexes in the string that
#have capital letters

#For example, calling capital_indexes('HeLlo') should return the list [0, 2, 4]

#---

#__mine__ (this is created by using my idea)
def capital_indexes(string):
    index           =   0
    capitalIndexes  =   []
    for characterItem in string:
        isUpper     =   str.isupper(characterItem)
        if isUpper :
            capitalIndexes.append(index)

        index += 1

    return capitalIndexes

string  =   input('Input String you want to operate\n')
capitalIndexes  =   capital_indexes(string=string)
print(capitalIndexes)
#end of __mine__