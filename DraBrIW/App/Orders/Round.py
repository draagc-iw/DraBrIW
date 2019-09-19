from ..User import User
from DraBrIW.App.Orders import Order
from DraBrIW.App.Storage import UserService

from DraBrIW.App.Utils.terminal_utils import bold
from DraBrIW.App.Utils.utils import generate_uid


class Round:
    def __init__(self, initiator: User):
        self._initiator = initiator
        self._orders = dict()
        self._uid = generate_uid()
        self.user_service = UserService()

    @property
    def uid(self):
        return self._uid

    @property
    def orders(self):
        return self._orders

    def new_round(self):
        self._initiator = None
        self._orders = dict()
        self._uid = generate_uid()

    def add(self, person: User, order: Order):
        self._orders[person.uid] = order

    def __str__(self):
        initiator_name = "No initiator" if self._initiator is None else self._initiator.name
        output = bold(f"\nYour round\t-\t{initiator_name}\n")
        output += f"{'▔' * len(output)}\n"

        for uid, order in self._orders.items():
            output += f"{self.user_service.get_with_uid(uid).name}\n\t{order}\n\n"

        return output
