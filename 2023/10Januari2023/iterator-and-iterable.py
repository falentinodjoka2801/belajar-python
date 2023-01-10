myList  =   [
    "Medan", "Jakarta", "Aceh", "Padang", "Kalimantan"
]
myIterator  =   iter(myList)

try:
    print(next(myIterator)) #Medan
    next(myIterator) #Jakarta
    next(myIterator) #Aceh
    next(myIterator) #Padang
    print(next(myIterator)) #Kalimantan
    # print(next(myIterator))

    myListAttributeAndMethod        =   dir(myList)
    myIteratorAttributeAndMethod    =   dir(myIterator)

    print(myListAttributeAndMethod)
    print('---')
    print(myIteratorAttributeAndMethod)

except StopIteration as stopIteration:
    print(stopIteration)

#Conclusion
#Iterator is iterable, but iterable is not iterator.
#Since iterator is concist of iterable, so iterator uses iterable to form an iterator.

#Iterator and Iterable can be looped in a for loop. And the value it returns when it's looped
#is a single element they contains. 

#Iterator has a dunder method called __next__, but iterable not.
#Iterator and iterable both have __iter__

#Iterator has a state, but iterable not.