
from DraBrIW.TerminalFrontend import TerminalHandler
from DraBrIW.App import App

from multiprocessing import Pipe
import sys

def main():
    app_conn, front_conn = Pipe()

    app = App(app_conn)
    frontend = TerminalHandler(front_conn)

    app.start()
    return_code = frontend.run()

    app.join()
    sys.exit(return_code)


if __name__ == '__main__':
    main()
