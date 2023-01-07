import getpass

_password   =   getpass.getpass('Enter your password ..\n')
# while _password != 'tino':
#     _password   =   getpass.getpass('Your password is invalid! Try again!')

while True:
    if _password == 'tino':
        break
    _password   =   getpass.getpass('Your password is invalid! Try again please ..\n')

print('All right!')