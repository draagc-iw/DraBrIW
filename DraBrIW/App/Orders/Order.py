from datetime import datetime
import random
from DraBrIW.App.Brews import Drink

from functools import reduce


class Order:
    def __init__(self):
        self._uid = datetime.now().microsecond + random.getrandbits(16)
        self.items = dict()

    @property
    def uid(self):
        return self._uid

    @property
    def total(self):
        return reduce(lambda total, dict_item: total + dict_item[0].get_cost() * dict_item[1],
                      self.items.items(), 0)  # don't really know how to unpack the dict tuple as lambda param

    def add_item(self, drink_id):
        if drink_id in self.items.keys():
            self.items[drink_id] += 1
        else:
            self.items[drink_id] = 1


