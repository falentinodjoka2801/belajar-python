class MakhlukHidup(Exception):
    pass

class Manusia(MakhlukHidup):
    pass

class Raja(Manusia):
    pass

class Pangeran(Raja):
    pass

for benda_hidup in [MakhlukHidup, Manusia, Raja, Pangeran]:
    try:
        raise benda_hidup
    except Pangeran:
        print('Pangeran')
    except Raja:
        print('Raja')
    except Manusia:
        print('Manusia')
    except MakhlukHidup:
        print('Makhluk Hidup')

#If a class, lets say A, extends a class, B, then B's exception is A's exception too cause A inherits B class. But A's exception isn't B's exception, cause B does not
#inherit A