import mysql
import os, sys
from mysql.connector import errorcode
import App.Utils as Utils
from App.Storage.db_utils import get_db_pass_from_keychain
SQL_connection_config = {
    'host': os.environ["MYSQL_HOST"],
    'user': os.environ["MYSQL_USER"],
    'database': os.environ["MYSQL_DB"],
    'password': os.environ.get("MYSQL_PASS") if os.environ.get("MYSQL_PASS") is not None else get_db_pass_from_keychain(),
    'port': os.environ.get("MYSQL_PORT") if os.environ.get("MYSQL_PORT") is not None else 3306,
}


class DBConnectionManager(metaclass=Utils.SingletonMeta):
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
                print("Invalid database credentials")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                
            print(err, file=sys.stderr, flush=True)
            sys.exit(err.errno)
        else:
            print("Connection to database successful")

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
