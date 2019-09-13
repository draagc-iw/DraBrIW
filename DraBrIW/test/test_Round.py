from DraBrIW.Orders.Round import Round
from DraBrIW.Orders.Order import Order
from DraBrIW.User import User

from DraBrIW.Brews import Americano, Espresso, DoubleEspresso

ROUND_SIZE = 15


class TestUser(User):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value


def build_round(round_size: int = None):
    rnd_size = round_size if round_size is not None else ROUND_SIZE
    test_initiator = TestUser("Test Initiator", Americano())
    test_round = Round(test_initiator)
    for idx in range(rnd_size):
        usr = TestUser(f"Round User {idx}", Americano())
        order = Order()
        order.add_item(Espresso())
        order.add_item(DoubleEspresso())
        order.add_item(Americano())
        test_round.add(usr, order)

    return test_round


def test_print():
    test_round = build_round()
    print(test_round)
