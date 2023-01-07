from smtplib import SMTP, SMTPException

_sender     =   'belajarpython2801@gmail.com'
_receivers  =   ['falentinodjoka2801@gmail.com', 'falentino@mahasiswa.pancabudi.ac.id']

_message    =   'Hello brother!'

try:
    _smtp   =   SMTP(host='smtp.gmail.com', port=587)
    _smtp.sendmail(from_addr=_sender, to_addrs=_receivers, msg=_message)
except SMTPException as e:
    print('Error : unable to send email!')
    print(e.strerror)