import argparse

from datetime import datetime
import random

# from ..User import User
from ZDraBrIW.TerminalFrontend.Menu import SubMenu, MenuManager


def get_round_initiator(menu_manager: MenuManager):
    menu = SubMenu("Select Initiator", menu_manager)


def parse_args():
    """
    Creates argument menu and returns parsed arguments
    :return: argparse.Namespace containing arguments
    """
    argp = argparse.ArgumentParser("Menu for BrIW")

    g_cmnds = argp.add_argument_group("Commands")
    g_cmnds.add_argument("--get-drinks", action="store_true")
    g_cmnds.add_argument("--get-people", action="store_true")

    return argp.parse_args()


def calc_width_cell(users: iter):
    max_len_name = _get_max_len(users, "name")
    max_len_drink = _get_max_len(users, "fav_drink")
    return max(max_len_name, max_len_drink) + 4


def _get_max_len(iterable: iter, prop: str):
    return max(map(lambda item: len(getattr(item, prop)), iterable))



def generate_uid():
    time_now = datetime.now().strftime("%-H%-M%-S%f")
    rand = str(random.getrandbits(8))
    return int(time_now + rand)
