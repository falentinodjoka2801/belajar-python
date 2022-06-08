import smtplib, getpass

_smtpObject =   smtplib.SMTP('smtp.gmail.com', port=587)
_smtpObject.ehlo()
_smtpObject.starttls()

_email      =   input('Input your email ...\n')
_password   =   getpass.getpass('Password please \n')

_receiver   =   input('Input receiver\'s email address ..\n')

_smtpObject.login(_email, _password)

_messageToSend  =   'Hello, this email comes from Python Script that you made'

_smtpObject.sendmail(_email, _receiver, _messageToSend)