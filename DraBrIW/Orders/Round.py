from ..User import User
from .Order import Order


class Round:
    def __init__(self, initiator: User):
        self._initiator = initiator
        self._orders = dict()

    def add(self, person: User, order: Order):
        self._orders[person] = order

    def __str__(self):
        output = f"Your round\t-\t{self._initiator}\n"
        for user, order in self._orders.items():
            output += f"{user}\n\t{order}\n\n"

        return output



