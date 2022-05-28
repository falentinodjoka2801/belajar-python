_list   =   [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
_list.sort()

if len(_list) % 2 == 0:
    _m1     =   _list[len(_list) // 2]
    _m2     =   _list[len(_list) // 2 - 1]
    _median     =   (_m1 + _m2) / 2
else:
    _median     =   _list[len(_list) // 2]

print(_median)