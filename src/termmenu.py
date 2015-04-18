import sys
import termios
import tty
from cStringIO import StringIO

UP = '\x1b[A'
DOWN = '\x1b[B'
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def f():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin.fileno())
        # escape sequences are 3 bytes long, but we might get an \n, so we check the first anyways
        ch = sys.stdin.read(1)
        if ch != '\n':
            ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_menu(position, options):
    sys.stdout = buf = StringIO()

    for i, o in enumerate(options):
        selector = '>> ' if i == position else '   '
        print selector, o

    sys.stdout = sys.__stdout__
    return buf.getvalue()[:-1]


erase_lines = lambda count: sys.stdout.write((CURSOR_UP_ONE + ERASE_LINE) * count)


def menu_prompt(options):
    position = 0

    while True:

        buf = print_menu(position, options)
        print buf

        v = f()
        if v == UP:
            position = max(0, position - 1)
        elif v == DOWN:
            position = min(position + 1, len(options) - 1)
        elif v[0] == '\n':
            return position
        else:
            print v[0], v[1], v[2]
            raw_input()

        erase_lines(len(options))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit(1)
    print menu_prompt(sys.argv[1:])
