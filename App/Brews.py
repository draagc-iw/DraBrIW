import abc
import enum


class Ingredients(enum.Enum):
    WATER = 0
    ESPRESSO = 1
    MILK_FOAM = 2
    MILK = 3
    CHOCOLATE_SYRUP = 4


class Brew(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_cost(self):
        pass

    @abc.abstractmethod
    def get_ingredients(self):
        pass

    def __str__(self):
        return self.get_name()


class BrewDecorator(Brew, metaclass=abc.ABCMeta):
    def __init__(self, decorated_object: Brew):
        self._decorated_obj = decorated_object
        self._name: str = "BrewDecorator"
        self._cost = 0

    def get_cost(self):
        return self._decorated_obj.get_cost() + self._cost

    def get_ingredients(self):
        return self._decorated_obj.get_ingredients()

    def get_name(self):
        drink_name = self._decorated_obj.get_name()
        if drink_name.find("- with -") == -1:
            drink_name += " - with - "
        else:
            drink_name += ", "
        drink_name += self._name

        return drink_name

    def __str__(self):
        return self.get_name()


class Drink(Brew):
    def __init__(self, name, price, id: int = None, ingredients=None):
        self.id = id
        self._name = name
        self._price = price
        self._ingredients = ingredients if ingredients is not None else list()

    def get_name(self):
        return self._name

    def get_ingredients(self):
        return self._ingredients

    def get_cost(self):
        return self._price

    def __str__(self):
        return f"#{self.id} - {self.get_name()}"
