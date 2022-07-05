from mysql.connector import connect

_connection     =   connect(host='localhost', user='root', password='', database='belajar-python')
_cursor         =   _connection.cursor()

_sql    =   'select * from karyawan where id="234"'
_cursor.execute(_sql)

_fetchAll   =   _cursor.fetchall()
print(_fetchAll)

_cursor.close()
_connection.close()