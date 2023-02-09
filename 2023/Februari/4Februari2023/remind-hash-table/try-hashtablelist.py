from hash_table_list import HashTableList

ht  =   HashTableList()
ht['january']   =   28
print(ht.data)
ht['november']  =   29
print(ht.data)
del ht['januar']
print(ht.data)
del ht['january']
print(ht.data)