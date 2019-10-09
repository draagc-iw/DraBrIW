from ..User import User
from App.Orders import Order
from App.Utils.terminal_utils import bold


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
        # print(object.__str__())
        if person.uid in self._orders.keys():
            for drink_id in order.items.keys():
                self._orders[person.uid].add_item(drink_id)
        else:
            self._orders[person.uid] = order


    def __str__(self):
        initiator_name = "No initiator" if self.initiator is None else self.initiator.full_name
        output = bold(f"\nYour round\t-\t{initiator_name}\n")
        output += f"{'▔' * len(output)}\n"

        # for uid, order in self._orders.items():
        #     output += f"{UserService().get_with_uid(uid).full_name}\n\t{order}\n\n"

        return output
