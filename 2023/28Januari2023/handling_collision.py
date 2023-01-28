from hash_table_list import HashTableList

t   =   HashTableList()
t['january']    =   28
t['january']    =   21
t['november']   =   29
t['desember']   =   25

print(t.array)
del t['january']
print(t.array)