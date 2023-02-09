list1   =   [(1, 2, 3), (4, 5, 6)]
print(list1)

first_address   =   hex(id(list1))
print(first_address)

list1[0]    =   (7, 8, 9)
print(list1)

second_address  =   hex(id(list1))
print(second_address)

print(first_address == second_address)