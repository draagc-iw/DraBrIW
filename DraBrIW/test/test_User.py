import unittest
from ZDraBrIW.App.Brews import Americano

from ZDraBrIW.App.User import User


class TestUser(unittest.TestCase):
    drink = Americano()

    def test_init(self):
        name = "Test Name"

        test_user = User(name, TestUser.drink)
        self.assertEqual(test_user.name, name)
        self.assertEqual(test_user.fav_drink, TestUser.drink)

    def test_badname(self):
        name = "#¢∞§¶£$%^& ª•%^#¢ª•("
        self.assertRaises(ValueError, User, name, TestUser.drink)

    def test_baddrink(self):
        name = "Test Name"
        drink = "Americano"
        self.assertRaises(ValueError, User, name, drink)
