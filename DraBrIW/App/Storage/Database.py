import os, sys
import yaml

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

            self.clean()

        else:
            self._db = dict()

    def save(self, path=None):
        path = self._path if path is None else path

        try:
            with open(path, "w") as file:
                yaml.dump(self._db, file)
        except IOError as e:
            print("Cannot save database to persistent storage")
            print(e)

    def clean(self):
        keys_to_remove = []
        for key, value in self._db.items():
            if value is None:
                keys_to_remove.append(key)
        for item in keys_to_remove:
            del self._db[item]


class BrewDatabase(Database):
    def __init__(self, db_name):
        super(BrewDatabase, self).__init__(db_name)
