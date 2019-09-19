import unittest
import unittest.mock as mock

from DraBrIW.Storage import UserService, UserDatabase
from DraBrIW.User import User
from DraBrIW.Brews import Americano, Espresso


class TestUserService(unittest.TestCase):

    def test_singleton(self):
        user_service1 = UserService()
        user_service2 = UserService()

        self.assertIs(user_service1, user_service2)

    def test_add_get_delete(self):
        us = UserService()

        user1 = User("Test User", Americano())
        user2 = User("Tess User", Americano())
        us.add(user1)
        us.add(user2)

        self.assertEqual(user1, us.get_with_uid(user1.uid))
        self.assertEqual(user2, us.get_with_uid(user2.uid))

        us.delete(user2)
        self.assertEqual(None, us.get_with_uid(user2.uid))

    def test_change_name(self):
        us = UserService()

        initial_name = "Old Name"
        user = User(initial_name, Americano())
        uid = user.uid

        us.add(user)

        new_name = "New Name"
        us.change_name(user.uid, new_name)
        self.assertEqual(us.get_with_uid(uid).name, new_name)

    def test_change_drink(self):
        us = UserService()

        initial_drink = Americano()
        user = User("Test User", initial_drink)
        uid = user.uid

        us.add(user)

        new_drink = Espresso()
        us.change_drink(uid, new_drink)

        self.assertEqual(new_drink, us.get_with_uid(uid).fav_drink)
