from ..User import User
from DraBrIW.App.Orders import Order
from DraBrIW.App.Utils.terminal_utils import bold
from DraBrIW.App.Utils.utils import generate_uid


class Round:
    def __init__(self, initiator: User, id: int = None):
        self.initiator = initiator
        self._orders = dict()
        self.id = id

    @property
    def uid(self):
        return self.id

    @property
    def orders(self):
        return self._orders

    def add(self, person: User, order: Order):
        self._orders[person.uid] = order

    def __str__(self):
        initiator_name = "No initiator" if self.initiator is None else self.initiator.full_name
        output = bold(f"\nYour round\t-\t{initiator_name}\n")
        output += f"{'▔' * len(output)}\n"

        # for uid, order in self._orders.items():
        #     output += f"{self.user_service.get_with_uid(uid).name}\n\t{order}\n\n"

        return output
