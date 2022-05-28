from mysql import connector

class Connection:
    def __init__(self):
        try:
            _connection     =   connector.connect(host='localhost', user='root', password='', database='laukpauk')
            self.connection =   _connection
            self.cursor     =   _connection.cursor()
        except:
            self.connection =   None
