def is_anagram(firstString: str, secondString: str):
    string1     =   list(firstString)
    string1.sort()
    string2     =   list(secondString)
    string2.sort()

    return string1 == string2

first: str  =   input('First String : ')
second: str =   input('Second String : ')

isAnagram   =   is_anagram(firstString=first, secondString=second)
if isAnagram:
    print('Yes')
else:
    print('No')