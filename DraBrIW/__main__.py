import os, sys

from DraBrIW.App.Storage import UserDatabase
from DraBrIW.TerminalFrontend.Menu import Menu, MenuItem, MenuManager, SubMenu
from DraBrIW.App.Utils.terminal_utils import int_input
# from DraBrIW.App.Utils.utils import clear_database, add_user_details
from DraBrIW.App.Brews import BREW_CLASSES, DECORATORS
from DraBrIW.App.Orders import OrderManager, RoundManager

from DraBrIW.Server import server_main


def main():
    db = UserDatabase("user_db")

    drinks = list(map(lambda item: item(), BREW_CLASSES))
    order_manager = OrderManager(drinks, DECORATORS)
    # round_manager = RoundManager()

    menu_manager = MenuManager()

    # Set-up Main Menu
    menu_main = Menu("☕ ∆ --- DraBrIW ⍺0.2 --- ∆ ☕", menu_manager)
    menu_main.add_item(MenuItem("Print database", lambda: print(db), "Prints the entire database"))
    # menu_main.add_item(MenuItem("Add new user", lambda: add_user_details(db), "Add a new user entry to the database"))
    # menu_main.add_item(MenuItem("Clear database", lambda: clear_database(db), "Deletes all entries in the database"))
    menu_main.add_item(MenuItem("Help", menu_main.print_help, "Prints this help message"))

    # Set-up Sub Menus
    submenu_order = SubMenu("Order Menu", menu_manager)
    submenu_order_single = SubMenu("New Order", menu_manager, order_manager.new_order)
    # submenu_order_round = SubMenu("New Round", menu_manager, round_manager.new_round)

    submenu_order.add_submenu(submenu_order_single)
    # submenu_order.add_submenu(submenu_order_round)

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


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == "--server":
        sys.exit(server_main())
    else:
        main()
