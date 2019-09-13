from ..User import User
import DraBrIW.Orders
from DraBrIW.Orders import RoundOrder

from DraBrIW.Utils.utils import generate_uid


class Round:
    def __init__(self, initiator: User):
        self._initiator = initiator
        self._orders = dict()
        self._uid = generate_uid()

    @property
    def uid(self):
        return self._uid

    def add(self, person: User, order: RoundOrder):
        self._orders[person] = order

    def __str__(self):
        output = f"\nYour round\t-\t{self._initiator.name}\n"
        output += f"{'▔' * len(output)}\n"

        for user, order in self._orders.items():
            output += f"{user.name}\n\t{order}\n\n"

        return output
