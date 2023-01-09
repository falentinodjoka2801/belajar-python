import pandas as pd

try:
    excelData   =   pd.read_excel('kpi-dosen-LayananMahasiswa-tahun_2021-2022.xlsx', sheet_name=['2022'])
    print(excelData)
except Exception as e:
    print('There\'s an error')
    print(e)