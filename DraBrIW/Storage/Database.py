import os, sys
import yaml
from DraBrIW.User import User
from DraBrIW.Utils import TableStringFormatter


class Database:
    def __init__(self, name=None):
        self._name = "db" if name is None else name
        self._path = "./{}.yaml".format(self._name)
        self._db = dict()
        self.load()

    def load(self, path=None):
        path = self._path if path is None else path

        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    self._db = yaml.load(f, Loader=yaml.FullLoader)
            except IOError as e:
                print("Unable to load database. In order to avoid database corruption, the program will now exit.")
                print(e)
                sys.exit(os.EX_IOERR)


        else:
            self._db = dict()

    def save(self, path=None):
        path = self._path if path is None else path

        try:
            with open(path, "w") as file:
                # pickle.dump(self._db, file)
                yaml.dump(self._db, file)
        except IOError as e:
            print("Cannot save database to persistent storage")
            print(e)


class UserDatabase(Database):
    def __init__(self, db_name):
        super(UserDatabase, self).__init__(db_name)

    def add(self, user: User):
        self._db[user.name] = user
        self.save()

    def get(self, name: str):
        if name in self._db.keys():
            return self._db[name]
        else:
            return None

    def clear(self):
        self._db = dict()
        self.save()

    def __str__(self):
        if len(self._db) is 0:
            return "Database empty 😢\n"
        printer = TableStringFormatter()
        printer.header(["PEOPLE", "DRINKS"])
        for item in self._db.values():
            printer.row([item.name, item.fav_drink])

        return printer.get()


class BrewDatabase(Database):
    def __init__(self, db_name):
        super(BrewDatabase, self).__init__(db_name)
