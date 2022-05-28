from PIL import Image
from math import floor, ceil

try:
    _oasisSomeMightSay  =   Image.open('../images/oasis-some-might-say.png')
    _oasisSomeMightSay.show(title='Gambar Original')

    _imageSize          =   _oasisSomeMightSay.size

    _imageWidth, _imageHeight     =   _imageSize

    _hCenter    =   _imageWidth / 2
    _vCenter    =   _imageHeight / 2
    
    _x  =   _hCenter - 100
    _y  =   _vCenter - 200
    _cropX  =   _hCenter + 100
    _cropY  =   _vCenter + 200

    _cropResult     =   _oasisSomeMightSay.crop((_x, _y, _cropX, _cropY))
    _cropResult.show(title='Gambar Crop')

    _cropSize               =   _cropResult.size
    _cropWidth, _cropHeight =   _cropSize   

    _oasisSomeMightSay.paste(im=_cropResult, box=(0, 0))
    _oasisSomeMightSay.paste(im=_cropResult, box=(floor(_imageWidth - _cropWidth), 0))
    _oasisSomeMightSay.paste(im=_cropResult, box=(floor(_imageWidth - _cropWidth), floor(_imageHeight - _cropHeight)))
    _oasisSomeMightSay.paste(im=_cropResult, box=(0, floor(_imageHeight - _cropHeight)))

    _oasisSomeMightSay.paste(im=_cropResult, box=(floor(_cropWidth), floor(_vCenter) - floor(_cropHeight / 2)))
    _oasisSomeMightSay.paste(im=_cropResult, box=(floor(_imageWidth - _cropWidth - _cropWidth), floor(_vCenter) - floor(_cropHeight / 2)))

    _oasisSomeMightSay.show(title='Hasil Tempelan')
except FileNotFoundError:
    print('File tidak ditemukan')