from enum import Enum
from DraBrIW.BaseBrew import Brew, BrewDecorator


class Ingredients(Enum):
    WATER = 0
    ESPRESSO = 1
    MILK_FOAM = 2
    MILK = 3
    CHOCOLATE_SYRUP = 4


class Espresso(Brew):
    def get_name(self):
        return "Espresso (Short Black)"

    def get_ingredients(self):
        return {Ingredients.ESPRESSO: 1}

    def get_cost(self):
        return 0


class DoubleEspresso(Brew):
    def get_name(self):
        return "Double Espresso (Doppio)"

    def get_ingredients(self):
        return {Ingredients.ESPRESSO: 2}

    def get_cost(self):
        return 0


class Americano(Brew):
    def get_cost(self):
        """FREE - It's InfinityWorks!"""
        return 0

    def get_ingredients(self):
        return {Ingredients.WATER: 1, Ingredients.ESPRESSO: 1}

    def get_name(self):
        return "Americano"


class Milk(BrewDecorator):
    name = "Milk"
    cost = 0.1

    def __init__(self, decorated_object):
        super(Milk, self).__init__(decorated_object)
        self._name = Milk.name
        self._cost = Milk.cost

    def get_ingredients(self):
        ingredients: list = self._decorated_obj.get_ingredients()
        ingredients.append(Ingredients.MILK)
        return ingredients

class Sugar(BrewDecorator):
    name = "Sugar"
    cost = 0.2

    def __init__(self, decorated_object):
        pass
BREW_CLASSES = [Espresso, DoubleEspresso, Americano]
DECORATORS = [Milk]

