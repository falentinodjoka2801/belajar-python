#character class is used for defining a set of some characters
#a character class is notated with a pair of this sign []

import re

_input      =    input('Input a character ...\n')
_pattern    =   '[^ace]'
if(re.search(_pattern, _input)):
    print('match!')
else:
    print('does not match')