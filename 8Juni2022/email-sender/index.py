from database.connections.belajar_python import BelajarPython
from smtplib import SMTP, SMTPAuthenticationError
from getpass import getpass

try:
    _bp             =   BelajarPython()
    _allKaryawan    =   _bp.runQuery('select * from karyawan')

    _smtpObject =   SMTP(host='smtp.gmail.com', port=587)
    _smtpObject.ehlo()
    _smtpObject.starttls()

    _senderUsername =   input('Input your email address\n')
    _senderPassword =   getpass('Password\n')
    _smtpObject.login(_senderUsername, _senderPassword)

    for _karyawan in _allKaryawan:
        _id, _nama, _alamat, _email =   _karyawan

        _msg    =   f'Hai {_nama} #{_id}, alamat anda di {_alamat}'
        _smtpObject.sendmail(_senderUsername, _email, _msg)

    _smtpObject.close()
except KeyboardInterrupt:
    print('Application was ended by user!')
except SMTPAuthenticationError:
    print('Username or Password you entered doesn\'t match!')