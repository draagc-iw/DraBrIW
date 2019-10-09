from ZDraBrIW.App.Storage import Database
from ZDraBrIW.App.User import User
from ZDraBrIW.App.Utils import TableStringFormatter

class UserDatabase(Database):
    def __init__(self, *args, **kw_args):
        super(UserDatabase, self).__init__(*args, **kw_args)

    def add(self, user: User):
        self._db[user.uid] = user
        self.save()

    def get_all(self) -> iter:
        return list(self._db.values())

    def get(self, uid: int) -> User:
        if uid in self._db.keys():
            return self._db[uid]
        else:
            return None

    def delete(self, uid: int):
        if uid in self._db.keys():
            self._db[uid] = None

    def clear(self):
        self._db = dict()
        self.save()

    def __str__(self):
        if len(self._db) is 0:
            return "Database empty 😢\n"
        printer = TableStringFormatter()
        printer.header(["PEOPLE", "DRINKS"])
        for item in sorted(self._db.values(), key=lambda i: i.name):
            printer.row([item.name, item.fav_drink])

        final_output = printer.get() + f"\n{len(self._db.keys())} entries"
        return final_output
