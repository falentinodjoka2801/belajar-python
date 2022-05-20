import getpass

_database   =   {
    "aman.kharwal"  :   "123456",
    "kharwal.aman"  :   "654321"
}
_username   =   input("Enter your username : ")
_password   =   getpass.getpass("Enter your pasword : ")

for i in _database.keys():
    if _username == i:
        while _password != _database.get(i):
            _password   =   getpass.getpass('Enter password again : ')
        break

print('Verified!')