#convert string that is separated by , into a list
#so the , sign is used to as a delimiter

_rawString  =   input('Input any string separated by , sign\n')
if ',' in _rawString:
    _list       =   _rawString.split(',')
    print(_list)

    def _generatorFunction(_listItem):
        return _listItem.strip()

    _mapObject  =   map(_generatorFunction, _list)
    _newList    =   list(_mapObject)
    
    print(_newList)
else:
    print('String')
    print(_rawString)

