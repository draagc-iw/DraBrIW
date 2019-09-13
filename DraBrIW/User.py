import re
from DraBrIW.BaseBrew import Brew


class User:
    def __init__(self, name, fav_drink: Brew):
        self.name = name
        self.fav_drink: Brew = fav_drink

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if len(new_value) > 30 or len(new_value) < 3:
            raise ValueError("Name length should be between 3 and 30 characters")
        re_name_validation = re.compile(r'^[^\W\d_]+(-[^\W\d_]+)?$', re.U)
        for item in new_value.split(" "):
            if not bool(re_name_validation.fullmatch(item)):
                raise ValueError("Invalid name")

        self._name = new_value

    @property
    def fav_drink(self):
        return self._fav_drink

    @fav_drink.setter
    def fav_drink(self, new_value):
        # if len(new_value) > 10 or len(new_value) < 3:
        #     raise ValueError("Drink length needs to be between 3 and 10 characters")
        self._fav_drink = new_value

    def __str__(self):
        return f"{self.name}\t|\t{self.fav_drink}"
