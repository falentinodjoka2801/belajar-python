from mysql import connector
from typing import Union

class BelajarPython():
    def __init__(self, host:str=None):
        _host       =   'localhost'
        if(host != None):
            _host   =   host

        _username   =   'root'
        _password   =   ''
        _database   =   'belajar-python'

        _connection     =   connector.connect(host=_host, user=_username, password=_password, database=_database)
        _cursor         =   _connection.cursor()

        self._connection     =   _connection
        self._cursor         =   _cursor
    
    def __del__(self):
        _connection     =   self._connection
        _connection.close()

    def runQuery(self, query:str, options:Union[None, dict]=None):
        _cursor         =   self._cursor
        _queryExecution =   _cursor.execute(query)

        _singleRow  =   False

        if options != None:
            if 'singleRow' in options:
                _singleRow  =   options['singleRow']

        if _singleRow:
            _queryResult    =   _cursor.fetchone()
        else:
            _queryResult    =   _cursor.fetchall()

        return _queryResult
    