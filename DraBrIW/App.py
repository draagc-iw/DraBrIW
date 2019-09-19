from DraBrIW.Storage import UserService, UserDatabase
from DraBrIW.User import User
from DraBrIW.TerminalFrontend.Menu import Menu, MenuItem, MenuManager, SubMenu
from DraBrIW.Utils.terminal_utils import int_input
from DraBrIW.Brews import BREW_CLASSES, DECORATORS, Americano
from DraBrIW.Orders import OrderManager, Round

import multiprocessing as mp
from multiprocessing.connection import Connection

drinks = list(map(lambda item: item(), BREW_CLASSES))

class App(mp.Process):
    def __init__(self, conn: Connection):
        super(App, self).__init__()
        self.conn: Connection = conn
        self.user_service = UserService()
        self.db = UserDatabase("user_db")
        self.order_manager = OrderManager(drinks, DECORATORS)

        self.events = {
            'print_db': lambda: str(self.db),
            'new_single_order': lambda: self.order_manager.new_order()
        }

    def run(self):
        while True:
            event = self.conn.recv()
            response = self.handle_event(event)
            self.conn.send(response)

    def handle_event(self, ev):
        if ev in self.events.keys():
            return self.events[ev]()
        return None
