from exercise_hash_table import ExerciseHashTable

ht  =   ExerciseHashTable()
ht['january']   =   28
print(ht['january'])
ht['november']  =   29
ht['january']   =   15
print(ht['january'])

print(ht.array)

del ht['january']
print(ht.array)