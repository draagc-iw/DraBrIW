import os, sys

from DraBrIW.TerminalFrontend import TerminalHandler
from DraBrIW.App import App

from multiprocessing import Pipe


def main():
    app_conn, front_conn = Pipe()

    app = App(app_conn)
    frontend = TerminalHandler(front_conn)

    app.start()
    sys.exit(frontend.run())


if __name__ == '__main__':
    main()
