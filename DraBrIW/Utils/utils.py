import argparse

import os
import pickle

from datetime import datetime
import random

from ..Storage.Database import UserDatabase
from ..User import User

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


def int_input(msg=""):
    try:
        choice = int(input(msg + '\n'))
    except ValueError:
        print("Invalid choice")
        return None
    return choice


def yes_no_prompt(msg: str):
    while True:
        answer = str(input(msg + "[y/n]"))
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")

def overwrite_drink(db: UserDatabase, name: str):
    drink = input("Enter your favourite drink:\n")
    db.add(User(name, drink))
    print("Your favourite drink has been changed.")


def add_user_details(db: UserDatabase):
    name = input("Enter your name:\n")
    if db.get(name) is None:
        drink = input("Enter your favourite drink:\n")
        db.add(User(name, drink))
        print(f"New user!{name.capitalize()}'s favourite drink is {drink}")
    else:
        prompt_msg = f"{name} already exists. Do you want to change your preference? [y/n]\n"
        yes_no_prompt(prompt_msg, lambda: overwrite_drink(db, name), lambda: print("No changes made"))


def clear_database(db: UserDatabase):
    ULTRA_SECURE_PASSWORD = "tabsnotspaces"
    passwd = input("This will erase the entire database. Please enter the password to proceed: \n")
    if passwd == ULTRA_SECURE_PASSWORD:
        db.clear()
        print("Congrats! All data is now lost!")
    else:
        print("Wrong password!\n")

def generate_uid():
    return datetime.now().microsecond + random.getrandbits(16)