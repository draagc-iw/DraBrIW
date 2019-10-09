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

def bold(string: str):
    return f"\033[1m{string}\033[0m"

