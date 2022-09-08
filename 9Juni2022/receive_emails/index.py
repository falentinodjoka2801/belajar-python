from imaplib import IMAP4_SSL, IMAP4
from email import message_from_string

try:
    _imap       =   IMAP4_SSL('imap.gmail.com')

    _email      =   'falentinodjoka2801@gmail.com'
    _password   =   'cklpnhawpmfphuqn'

    _imap.login(_email, _password)
    
    _imap.select('INBOX')
    _type, _data    =   _imap.search(None, 'FROM "admin@sinovakno.com"')

    _emailID_bytesString:bytearray  =   _data[0]
    _emailID_regularString          =   _emailID_bytesString.decode()
    _emailID_list   =   _emailID_regularString.split(' ')

    def _emailIDGenerator(emailId):
        return emailId

    _mapObject      =   map(_emailIDGenerator, _emailID_list)
    _listEmailID    =   list(_mapObject)

    if len(_listEmailID) >= 1:

        _nomorUrut  =   1
        for _emailID in _listEmailID:
            _emailData              =   _imap.fetch(_emailID.encode(), '(RFC822)')
            _type, _dataOfEmail     =   _emailData
            
            _rawEmail           =   _dataOfEmail[0][1]
            _encodedEmailString =   _rawEmail.decode('utf-8')

            _emailTree          =   message_from_string(_encodedEmailString)
            _emailTreeIterable  =   _emailTree.walk()
            for _part in _emailTreeIterable:
                _body   =   _part.get_payload()

                _emailFile  =   open(f'emails/email_{_nomorUrut}.txt', mode='w')
                _emailFile.write(_body)
                _emailFile.close()

            _nomorUrut += 1
            
except IMAP4.error as e:
    print('IMAP Error!')
    print(e)