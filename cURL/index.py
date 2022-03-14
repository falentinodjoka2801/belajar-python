import requests

_getJadwalDelivery      =   requests.get('https://app.laukpauk.id/admin/API/JadwalDelivery/getAvailableJadwalDelivery')
try:
    _jadwalDelivery         =   _getJadwalDelivery.json()

    print(_jadwalDelivery)
    print(type(_jadwalDelivery))
    print(_jadwalDelivery['availableJadwalDelivery'][1])
except:
    print('Oops! Error occured!');
    print(_getJadwalDelivery.status_code)