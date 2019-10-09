from DraBrIW.App.Utils import SingletonMeta
from DraBrIW.App.Storage import DBConnectionManager
from DraBrIW.App.Brews import Drink
from DraBrIW.App.Utils import DrinkMapper


class DrinkService(metaclass=SingletonMeta):
    def __init__(self):
        self._db = DBConnectionManager()

    def add(self, drink_name):
        add_query = f"""INSERT INTO drinks (name) 
                       VALUES (%s);"""
        cursor = self._db.cursor_prepared
        cursor.execute(add_query, (drink_name,))


    def get(self, uid: int):
        get_uid_q = f""" SELECT 
                            id, name
                        FROM drinks
                        WHERE id = {uid};
                    """

        cursor = self._db.cursor_named
        cursor.execute(get_uid_q)
        return DrinkMapper.from_db(cursor.fetchone())

    def get_all(self):
        get_all_q = """ SELECT 
                            id, name
                        FROM drinks
                    """

        cursor = self._db.cursor_named
        cursor.execute(get_all_q)
        return list(map(lambda row: DrinkMapper.from_db(row), cursor.fetchall()))
