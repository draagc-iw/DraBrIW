from .Order import Order

from DraBrIW.App.Brews import Brew, BrewDecorator
from DraBrIW.App.Utils import TableStringFormatter
from DraBrIW.App.Utils.terminal_utils import int_input, yes_no_prompt


class OrderManager:
    def __init__(self, drinks: list, decorators: list):
        self._order = None
        self._drinks = self._index_items(drinks)
        self._decorators = self._index_items(decorators)

    def new_order(self):
        self._order = Order()
        return self.get_menu_string()

    def add_to_order(self):
        drink = self._get_drink()

        cont = yes_no_prompt("Add extras?\n")
        while cont:
            new_drink = self._get_decorator(drink)
            drink = new_drink if new_drink is not None else drink
            cont = yes_no_prompt("Add more extras?\n")

        self._order.add_item(drink)
        self.print_order()

    def _get_decorator(self, drink: Brew):
        self.print_decorators()

        choice = int_input("Enter your choice of extras")
        if choice not in self._drinks.keys():
            print("Invalid choice")
            return None
        decorator_class: BrewDecorator.__class__ = self._decorators[choice]
        return decorator_class(drink)

    def _get_drink(self):
        # self.get_menu_string()

        choice = int_input("Enter your choice of drink")
        if choice not in self._drinks.keys():
            print("Invalid choice")
            return
        return self._drinks[choice]

    def _index_items(self, items: iter):
        return dict(zip([i for i in range(len(items))], items))

    def get_menu_string(self):
        table_formatter = TableStringFormatter()
        table_formatter.header(["No.", "Name", "Price", "Ingredients"])

        for index, drink in self._drinks.items():
            ingredients_str = str()
            for key, value in drink.get_ingredients().items():
                ingredients_str += f"{value}x{key.name} "
            table_formatter.row([index, drink.get_name(), drink.get_cost(), ingredients_str])

        return table_formatter.get()

    def print_order(self):
        if self._order is not None:
            print(self._order)

    def print_decorators(self):
        print("Extras:\n")
        table_formatter = TableStringFormatter()
        table_formatter.header(["No.", "Name", "Price"])
        for index, decorator in self._decorators.items():
            table_formatter.row([index, decorator.name, decorator.cost])

        print(table_formatter.get())
