from ..Utils import SingletonMeta
import DraBrIW.App.User as _User
from DraBrIW.App.Storage import UserDatabase

from ..BaseBrew import Brew


class UserService(metaclass=SingletonMeta):
    def __init__(self, database: UserDatabase = None):
        self._db: UserDatabase = database if database is not None else UserDatabase('user_db')

    def add(self, user: _User.User):
        if self._db.get(user.uid) is not None:
            raise ValueError("User already exists")
        self._db.add(user)

    def get_with_uid(self, uid) -> _User.User:
        return self._db.get(uid)

    def get_with_name(self, name) -> list:
        results = [user for user in self._db.get_all() if user.name == name]
        return results

    def delete(self, user: _User.User):
        self._db.delete(user.uid)

    def change_name(self, uid, new_name: str):
        user = self._db.get(uid)
        user.name = new_name
        self._db.add(user)

    def change_drink(self, uid, new_drink: Brew):
        user = self._db.get(uid)
        user.fav_drink = new_drink
        self._db.add(user)


