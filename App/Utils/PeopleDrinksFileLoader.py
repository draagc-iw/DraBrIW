import os

from App.User import User
from App import CustomDrink
from App.Storage import UserDatabase


class BufferedUserDatabase(UserDatabase):
    def add(self, user: User):
        self._db[user.uid] = user


class PeopleDrinksFileLoader:
    def __init__(self, path: str, people_filename="people.txt", drinks_filename="drinks.txt"):
        self.path = path
        self.people_filename = people_filename
        self.drinks_filename = drinks_filename

    def load(self):
        people_path = os.path.join(self.path, self.people_filename)
        drinks_path = os.path.join(self.path, self.drinks_filename)
        if not os.path.exists(people_path):
            raise ValueError(f"No such file {people_path}")
        elif not os.path.exists(drinks_path):
            raise ValueError(f"No such file {drinks_path}")

        db = BufferedUserDatabase("user_db")
        try:
            with open(people_path, 'r') as people_file, open(drinks_path, 'r') as drinks_file:
                for person_name, drink_name in zip(people_file.readlines(), drinks_file.readlines()):
                    drink = CustomDrink(drink_name.strip("\n\r"), 0)
                    user = User(person_name.strip("\n\r"), drink)
                    db.add(user)

                db.save()
        except IOError as e:
            print(f"Error encountered while opening files\n{e}")


if __name__ == '__main__':
    os.system("pwd")
    pdfl = PeopleDrinksFileLoader("./")
    pdfl.load()
