#__mine__
#i have tried to count a number of element of myIterator variable (list_iterator type) by using len() function
#cause I suggest everything in python is an object, iterator is an object, and len() function needs an object as its parameter
#So i tried it, and an exception occured.

# try:
#     myList      =   [1, 2, 3, 4, 5] #iterable
#     myIterator  =   iter(myList) #iterator
#     print(len(myList))
#     print(len(myIterator))
# except Exception as e:
#     print(e)

#end of __mine__

#I will try to use enumerate() with my iterator. Enumerate returns an enumerate objects.
#If you 

myList      =   [1, 2, 3, 4, 5] #iterable
myIterator  =   iter(myList) #iterator

iteratorEnumerate   =   enumerate(myList, start=3)
print(len(list(iteratorEnumerate)))