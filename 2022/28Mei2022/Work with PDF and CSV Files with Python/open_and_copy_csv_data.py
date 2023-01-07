from csv import reader, writer

_openedFile =   open('../../documents/csv/kode-pos-indonesia.csv', encoding='utf-8')
_reader     =   reader(_openedFile)

_fileKecamatanProvinsi  =   open('../../documents/csv/file-kecamatan-provinsi.csv', mode='w', newline='')
_fileKecProvWriter      =   writer(_fileKecamatanProvinsi)

_dataCSV    =   list(_reader)
for rowKodePosIndonesia in _dataCSV:
    _row    =   [rowKodePosIndonesia[0], rowKodePosIndonesia[2], rowKodePosIndonesia[5]]
    _fileKecProvWriter.writerow(_row)

_openedFile.close()
_fileKecamatanProvinsi.close()