month   =   ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November')
print(hex(id(month)))

month   =   month + tuple('December')
print(hex(id(month)))

#the both first id, and second id are not same. It cause the immutability of tuple in python.
#Tuple in python is immutable. If you try to change the value of the tuple, it can occur an exception. If you try to merge one tuple with another tuple
#it can be done, but the address of tuple will be change, it cause the immutability of tuple.

#Immutable means the object's value cannot be changed with the same memory address. Mutable is the reverse, it can be changed with the same memory address.