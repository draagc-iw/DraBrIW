from datetime import datetime
import random
from DraBrIW.App.BaseBrew import Brew

from functools import reduce


class Order:
    def __init__(self):
        self._uid = datetime.now().microsecond + random.getrandbits(16)
        self._order_items = dict()

    @property
    def uid(self):
        return self._uid

    @property
    def total(self):
        return reduce(lambda total, dict_item: total + dict_item[0].get_cost() * dict_item[1],
                      self._order_items.items(), 0)  # don't really know how to unpack the dict tuple as lambda param

    def add_item(self, item: Brew):
        if item in self._order_items.keys():
            self._order_items[item] += 1
        else:
            self._order_items[item] = 1

    def __str__(self):
        output = f"Your Order -- id. {self._uid}\n"
        output += f"{'▔' * 25}\n"

        for drink, count in self._order_items.items():
            output += f"{drink.get_name()}\n\t\t{count}x\t£{drink.get_cost()}\n"

        output += f"Total: {self.total}"
        return f"\n{output}\n"


