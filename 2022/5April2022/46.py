# _stockPrices    =   [
#     ('Apple', 200), ('Google', 400), ('Microsoft', 100)
# ]

# for _item in _stockPrices:
#     print(_item)

# for _merk, _price in _stockPrices:
#     print('Produk {}, harga {}'.format(_merk, _price))

_workHoursPerMonth  =   [
    ('Falentino', 1500), ('Andrian', 300), ('Samson', 700), ('Tini', 250),
    ('Syahdan', 100), ('Merry', 3020), ('Samuel', 1000), ('Mega', 1000)
]

def _greatesEmployee(workHour):
    _current_max        =   0
    _employeeOfTheMonth =   ''

    for employeeName, hour in workHour:
        if(hour > _current_max):
            _current_max        =   hour
            _employeeOfTheMonth =   employeeName

    return (_employeeOfTheMonth, _current_max)

_bestEmployee   =   _greatesEmployee(_workHoursPerMonth)
print(_bestEmployee)