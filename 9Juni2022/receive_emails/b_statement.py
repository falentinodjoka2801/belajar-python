#b statement in front of a string means that string is a bytes string
#bytes string is different between regular string that we know
#regular string has an ASCII Character, meanwhile bytes string doesn't

#bytes string is an array of byte variable

#we can convert regular string to bytes string with built in encode method in a string object
_name = 'Tino'
print(_name)
print(_name.encode())

#also, we can convert regular string to bytes string with b statement
_string     =   b'Hello'
print(_string)