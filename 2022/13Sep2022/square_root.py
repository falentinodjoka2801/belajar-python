# _rootValue  =   sqrt(25)
# print(_rootValue)

def mySqrt(value):
    _left       =   1
    _right      =   value
    _mid        =   0

    while(_left <= _right):
        _mid    =   (_left + _right) // 2

        if(_mid * _mid == value):
            return _mid
        elif(_mid * _mid > value):
            _right  =   _mid - 1
        else:
            _left   =   _mid + 1
            _sqrt   =   _mid
    
    return _sqrt

print(mySqrt(25))


#Cara Kerja
#1. Melakukan pengecekan berulang dalam rentang nilai tertentu (nilai awal sd nilai akhir)
#2. Menentukan titik tengah (nilai tengah) dari rentang nilai sebelumnya
#3. Nilai tengah yg sudah ditentukan sebelumnya dilakukan pengecekan sbb :
#   3.1 Apakah nilai tengah kuadrat sama dengan nilai VALUE
#       ->  Ya => return nilai tengah tsb, 
#           Tidak => lakukan pengecekan 3.2
#   3.2 Apakah nilai tengah kuadrat lebih besar dari nilai VALUE
#       ->  Ya => lakukan pengecekan dari awal dengan rentang akhir = nilai tengah - 1, 
#           Tidak => lakukan langkah 3.3
#   3.3 Set rentang awal menjadi nilai tengah + 1 dan nilai sqrt = nilai tengah tsb