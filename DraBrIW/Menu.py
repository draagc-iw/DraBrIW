class MenuItem:
    def __init__(self, name: str, action: callable, msg_help: str = None):
        self._name = name
        self._action = action
        self._number = 0
        self._msg_help = msg_help

    def run_action(self):
        self._action()

    @property
    def name(self):
        return self._name

    @property
    def msg_help(self):
        return self._msg_help

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


class Menu:
    def __init__(self, name: str, manager):
        self._name = name
        self._items = dict()
        if type(manager) is not MenuManager:
            raise ValueError("Type of manager needs to be MenuManager")
        self._manager: MenuManager = manager

    def add_item(self, item: MenuItem):
        item.number = len(self._items)
        self._items[item.number] = item

    def run_action(self, choice: int):
        if choice in self._items.keys():
            self._items[choice].run_action()
        else:
            print("Invalid choice")

    def print_help(self):
        output = ""
        for item in self._items.values():
            output += f"{item.name}\n\t{item.msg_help}\n"
        output += "\n"

        print(output)

    def add_submenu(self, submenu):
        if type(submenu) is not SubMenu:
            raise ValueError("Argument must be of type SubMenu")

        submenu.parent_menu = self
        self.add_item(MenuItem(submenu.name, lambda: self.manager.change_menu(submenu)))

    @property
    def name(self):
        return self._name

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, new_manager):
        self._manager = new_manager

    def __str__(self):
        out = f"{self._name}\n"
        out += '▔' * len(self._name) + '\n'
        for item in self._items.values():
            out += f"[{item.number}] {item.name}\n"
        return out


class SubMenu(Menu):
    def __init__(self, name: str, manager, default_action: callable = None):
        super(SubMenu, self).__init__(name, manager)
        self._parent_menu: Menu = None
        self._default_action = default_action
        super(SubMenu, self).add_item(MenuItem("Back", lambda: self.manager.change_menu(self._parent_menu)))

    def default(self):
        if self._default_action is not None:
            self._default_action()

    def add_item(self, item: MenuItem):
        back_item = self._items.popitem()
        super(SubMenu, self).add_item(item)
        super(SubMenu, self).add_item(back_item[1])

    @property
    def parent_menu(self):
        return self._parent_menu

    @parent_menu.setter
    def parent_menu(self, new_value):
        self._parent_menu = new_value


class MenuManager:
    def __init__(self):
        self._main_menu: Menu = None
        self._current_menu = self._main_menu

    def set_main_menu(self, main_menu):
        self._main_menu = main_menu
        self._main_menu.manager = self
        self._current_menu = self._main_menu

    def change_menu(self, to_menu: Menu):
        to_menu.manager = self
        self._current_menu = to_menu
        if type(self._current_menu) is SubMenu:
            self._current_menu.default()

    def run_action(self, choice: int):
        self._current_menu.run_action(choice)

    def print_menu(self):
        print(self._current_menu)
