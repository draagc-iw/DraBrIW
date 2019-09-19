import unittest

from DraBrIW.App.Orders import Round, RoundOrder
from DraBrIW.App.User import User

from DraBrIW.App.Brews import Americano, Espresso, DoubleEspresso


class TestUser(User):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value


class TestRound(unittest.TestCase):
    def build_order(self):
        order = RoundOrder()
        order.add_item(Espresso())
        order.add_item(DoubleEspresso())
        order.add_item(Americano())

        return order

    def build_round(self, round_size=15):
        self.test_initiator = TestUser("Test Initiator", Americano())
        test_round = Round(self.test_initiator)
        for idx in range(round_size):
            usr = TestUser(f"Round User {idx}", Americano())
            test_round.add(usr, self.build_order())

        return test_round

    def test_add_empty(self):
        test_round = self.build_round(0)
        round_user = TestUser("Round User", Americano())
        order = self.build_order()
        test_round.add(round_user, order)

        expected_orders = {round_user.uid: order}
        self.assertEqual(test_round.orders, expected_orders)

    def test_add_many(self):
        test_round = self.build_round(100)

        current_orders = test_round.orders.copy()
        new_orders = {}

        for idx in range(100):
            round_user = TestUser(f"Round User {idx}", Americano())
            order = self.build_order()
            new_orders[round_user.uid] = order
            test_round.add(round_user, order)

        expected_orders = dict(current_orders)
        expected_orders.update(new_orders)

        self.assertEqual(test_round.orders, expected_orders)

    def test_print(self):
        test_round = self.build_round()
        print(test_round)
