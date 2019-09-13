import os, sys

from DraBrIW.Storage.Database import UserDatabase
from DraBrIW.User import User
from DraBrIW.Menu import Menu, MenuItem, MenuManager, SubMenu
from DraBrIW.Utils.terminal_utils import yes_no_prompt, int_input
from DraBrIW.Utils.utils import clear_database, add_user_details
from DraBrIW.Brews import BREW_CLASSES, DECORATORS
from DraBrIW.Orders import OrderManager


db = UserDatabase("user_db")

drinks = list(map(lambda item: item(), BREW_CLASSES))
order_manager = OrderManager(drinks, DECORATORS)

menu_manager = MenuManager()

# Set-up Main Menu
menu_main = Menu("☕ ∆ --- DraBrIW ⍺0.2 --- ∆ ☕", menu_manager)
menu_main.add_item(MenuItem("Print database", lambda: print(db), "Prints the entire database"))
menu_main.add_item(MenuItem("Add new user", lambda: add_user_details(db), "Add a new user entry to the database"))
menu_main.add_item(MenuItem("Clear database", lambda: clear_database(db), "Deletes all entries in the database"))
menu_main.add_item(MenuItem("Help", menu_main.print_help, "Prints this help message"))

# Set-up Sub Menus
submenu_order = SubMenu("Order Menu", menu_manager)
submenu_order_single = SubMenu("New Order", menu_manager, order_manager.new_order)
submenu_order_round = SubMenu("New Round", menu_manager)

submenu_order.add_submenu(submenu_order_single)
submenu_order.add_submenu(submenu_order_round)

menu_main.add_submenu(submenu_order)

submenu_order_single.add_item(MenuItem("Order Item", order_manager.add_to_order))


# submenu_order.add_item(MenuItem("Order Item", order_manager.add_to_order))

# submenu_order.add_item(MenuItem("New Order", order_manager.new_order))

menu_main.add_item(MenuItem("Exit", lambda: sys.exit(0), "Exit the program"))
menu_manager.set_main_menu(menu_main)

os.system("clear")

while True:
    menu_manager.print_menu()
    choice = int_input("Choice:")

    os.system("clear")

    try:
        menu_manager.run_action(choice)
    except ValueError as e:
        print(e)


