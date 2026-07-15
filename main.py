import sys

from console_mvc.view.console_view import ConsoleView


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")
    ConsoleView().run()


if __name__ == "__main__":
    main()
