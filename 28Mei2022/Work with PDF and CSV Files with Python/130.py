import csv

_openedFile     =   open('../../documents/csv/example.csv', encoding='utf-8')
_csvData        =   csv.reader(_openedFile)
_dataLines      =   list(_csvData)

print(_dataLines[3:5])