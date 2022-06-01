from csv import reader, writer
from mysql import connector
import time

_openedFile     =   open('karyawan.csv', mode='r', encoding='utf-8')
_reader         =   reader(_openedFile)

_dataKaryawan   =   list(_reader)
_openedFile.close()

_connector  =   connector.connect(user='root', password='', host='localhost', database='belajar-python')
_cursor     =   _connector.cursor()

if(len(_dataKaryawan) >= 1):
    for _karyawan in _dataKaryawan:
        _insertQuery    =   'insert into karyawan (nama, alamat) values (%s, %s)'
        _cursor.execute(_insertQuery, (_karyawan[1], _karyawan[2]))
        _connector.commit()
else:
    print('Tidak ada data karyawan')

_openedFileToWrite  =   open('karyawan-from-db.csv', mode='w', newline='')
_writer     =   writer(_openedFileToWrite)

_sql    =   'select * from karyawan'
_cursor.execute(_sql)
_dataKaryawanFromDB     =   _cursor.fetchall()  
if(len(_dataKaryawanFromDB) >= 1):
    for _karyawanFromDB in _dataKaryawanFromDB:
        _id, _nama, _alamat =   _karyawanFromDB

        _row    =   (_id, _nama, _alamat)
        _writer.writerow(_row)

_openedFileToWrite.close()