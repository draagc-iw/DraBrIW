from App.Storage import DBConnectionManager
from App.User import User
from App.Brews import Brew
from App.Utils.Mappers import UserMapper


class UserService:
    def __init__(self):
        self._db = DBConnectionManager()

    def add(self, user: User):
        add_query = f"""INSERT INTO person (first_name, last_name, id_fav_drink) 
               VALUES (%s, %s, %s);"""
        cursor = self._db.cursor_prepared
        cursor.execute(add_query, UserMapper.to_db(user))
        self._db.commit()

    def get_with_name(self, name) -> list:
        pass

    def get_with_uid(self, uid) -> User:
        get_uid_q = f"""SELECT
                            p.id, p.first_name AS first_name, p.last_name AS last_name, d.name AS drink_name
                        FROM person AS p
                        LEFT JOIN drinks as d
                        ON p.id_fav_drink = d.id
                        WHERE p.id = {uid}"""

        cursor = self._db.cursor_named
        cursor.execute(get_uid_q)
        return UserMapper.from_db(cursor.fetchone())

    def get_all(self) -> list:
        get_all_q = f"""SELECT
                            p.id, p.first_name AS first_name, p.last_name AS last_name, d.name AS drink_name
                        FROM person AS p
                        LEFT JOIN drinks as d
                        ON p.id_fav_drink = d.id"""

        cursor = self._db.cursor_named
        cursor.execute(get_all_q)
        return list(map(lambda row: UserMapper.from_db(row), cursor.fetchall()))

    def change_drink(self, uid, new_drink_id):
        print(f"Change drink for {uid} to {new_drink_id}")
        update_drink_q = f""" UPDATE person
        SET id_fav_drink = ?
        WHERE id = ?
        """
        cursor = self._db.cursor_prepared
        cursor.execute(update_drink_q, (new_drink_id, uid))
        self._db.commit()


    def change_name(self, uid, new_name: str):
        pass

    def delete(self, user: User):
        pass

