import unittest

from ZDraBrIW.TerminalFrontend.Menu import Menu, MenuItem, MenuManager


class TestMenuItem(unittest.TestCase):
    def __init__(self, *args, **kw_args):
        super(TestMenuItem, self).__init__(*args, **kw_args)

        self.name = "Test Menu Entry"
        self.action = lambda: "Test Return Value"
        self.help = "Test Help Message"

    def build_MenuItem(self):
        return MenuItem(self.name, self.action, self.help)

    def test_name(self):
        menu_item = self.build_MenuItem()
        self.assertEqual(menu_item.name, self.name)

    def test_action(self):
        menu_item = self.build_MenuItem()
        self.assertEqual(menu_item.run_action(), self.action())

    def test_number(self):
        menu_item = self.build_MenuItem()
        menu_item.number = 5
        self.assertEqual(menu_item.number, 5)

    def test_help(self):
        menu_item = self.build_MenuItem()
        self.assertEqual(menu_item.msg_help, self.help)


class TestMenu(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMenu, self).__init__(*args, **kwargs)
        self.name = "Test Menu"
        self.test_menu_manger = MenuManager()

    def build_Menu(self) -> Menu:
        return Menu(self.name, self.test_menu_manger)

    def build_Menu_with_items(self, num_items=50) -> Menu:
        test_menu = self.build_Menu()

        for idx in range(num_items):
            menu_item = MenuItem(f"Menu Item {idx}", lambda: f"Test Action {idx}")
            test_menu.add_item(menu_item)

        return test_menu

    def test_name(self):
        test_menu = self.build_Menu()
        self.assertEqual(test_menu.name, self.name)

    def test_manager(self):
        test_menu = self.build_Menu()
        self.assertIs(test_menu.manager, self.test_menu_manger)

    def test_add(self):
        test_menu = self.build_Menu_with_items()