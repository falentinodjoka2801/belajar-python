# myList =    [None for _ in range (15)]
# myList1 =   []
# for _ in range(15):
#     myList1.append(None)

# print(myList)
# print(myList1)
# print(myList == myList1)

max     =   1000
def getHash(stringKey):
    h   =   0
    for char in stringKey:
        h   +=  ord(char)
    return h % max

print(getHash('march 6'))