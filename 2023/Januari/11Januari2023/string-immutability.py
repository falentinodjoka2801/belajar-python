try:
    myString    =   'Falentino Djoka'
    print(myString)
    myString[9] =   '-'
    print(myString)
except TypeError as e:
    print(e)

#String is immutable. String is also included to an Iterable type. So if you set an item (by an index) to a new value (char), it will raise an exception (TypeError) 