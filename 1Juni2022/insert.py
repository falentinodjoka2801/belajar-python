from mysql import connector

_connection     =   connector.connect(host='localhost', user='root', password='', database='belajar-python')
_cursor         =   _connection.cursor()

_sql    =   'update karyawan set alamat="Bundaran HI" where alamat="Jakarta" and nama="Tino"'

try:
    _cursor.execute(_sql)
    _affectedRows   =   _cursor.rowcount
    print(_affectedRows)
    _connection.commit()
except:
    _connection.rollback()

_connection.close()