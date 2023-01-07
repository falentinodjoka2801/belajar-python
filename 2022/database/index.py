from libraries.connection.laukpauk import Connection

_lP     =   Connection()
if(_lP.connection != None):
    _c      =   _lP.cursor

    _sql        =   'select id, nama, isSeller from view_user'
    _c.execute(_sql)
    _listUser   =   _c.fetchall()

    print(_listUser)
else:
    print('Something wrong occured!')