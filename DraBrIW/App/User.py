from DraBrIW.App.Brews import Brew


class User:
    def __init__(self, first_name, last_name, fav_drink: Brew = None, uid=None):
        self._uid = uid
        self.first_name = first_name
        self.last_name = last_name
        if fav_drink is not None:
            self.fav_drink: Brew = fav_drink
        else:
            self._fav_drink = None

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def uid(self):
        return self._uid

    @property
    def fav_drink(self):
        return self._fav_drink

    @fav_drink.setter
    def fav_drink(self, new_value: Brew):
        if not isinstance(new_value, Brew):
            raise ValueError("Favourite drink has to be a brew")
        self._fav_drink = new_value

    def __str__(self):
        return f"{self.full_name}\t|\t{self.fav_drink}"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        if self.uid == other.uid:
            return True
        return False
