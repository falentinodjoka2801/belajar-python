exampleString   =   '   xxxFalentino---    '
print(id(exampleString))
exampleString   =   exampleString.strip()
print(id(exampleString))
exampleString   =   exampleString.removeprefix('xxx')
print(id(exampleString))
exampleString   =   exampleString.removesuffix('---')
print(id(exampleString))
print(exampleString)

#Conclusion
#If you try to call strip(), or removeprefix(), or removesuffix method from a string,
#It won't affect to original string, it is called string immutability.
# But if you assign the same variable name to a brand new value, it will affect your string value
# #cause you have changed the originility of a string you made first 