myList  =   [1, 8, 2, 4, 11, 9, 3, 5, 12, 15, 6]
myList.sort()

print('Sorted myList')
print(myList)

lowest  =   myList[0]
highest =   None

indexData   =   0
for i in myList:
    isBerurutanDenganBilanganSelanjutnya     =   (i + 1) == myList[indexData + 1]
    if not isBerurutanDenganBilanganSelanjutnya:
        highest =   i
        break

    indexData += 1

lowestAndHighest    =   [lowest, highest]

print('Lowest and Highest')
print(lowestAndHighest)