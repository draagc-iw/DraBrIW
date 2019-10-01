import mysql
from mysql.connector import errorcode

from DraBrIW.App.Utils import SingletonMeta
from DraBrIW.App.Storage.db_utils import get_db_pass_from_keychain

SQL_connection_config = {
    'host': 'database-academy-test.crtvvzmhs8i6.eu-west-2.rds.amazonaws.com',
    'user': 'dragos',
    'database': 'dragos',
    'password': get_db_pass_from_keychain()
}


class DBConnectionManager(metaclass=SingletonMeta):
    def __init__(self):
        self._cnx: mysql.connector.MySQLConnection = None
        self.connect(SQL_connection_config)

    def check_connection(self):
        if not self._cnx.is_connected():
            self.connect(SQL_connection_config)


    def connect(self, connection_config):
        try:
            self._cnx = mysql.connector.connect(**connection_config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def commit(self):
        self._cnx.commit()

    @property
    def cursor_named(self) -> mysql.connector.connection.CursorBase:
        self.check_connection()
        return self._cnx.cursor(named_tuple=True)

    @property
    def cursor_prepared(self) -> mysql.connector.connection.CursorBase:
        self.check_connection()
        return self._cnx.cursor(prepared=True)

