#!python
"""
Command line menu prompt.
Produces a multi-option prompt with selection possible through keyboard UP and DOWN strokes.

- The function menu_prompt returns the index of the selected option.
- If called as a script, prints to stdout the option (useful to build interactive shells scripts from languages othar 
than Python).

Example as shell utility: 
$ python -m consolemenu "asdf" "qwer" "foo" "bar bababa?"


"""

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
        # escape sequences are 3 bytes long, but we might get an \n and want to bail out immediatelly.
        ch = sys.stdin.read(1)
        if ch != '\n':
            ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def __print_menu(position, options):
    sys.stdout = buf = StringIO()

    for i, o in enumerate(options):
        selector = '>> ' if i == position else '   '
        print selector, o

    sys.stdout = sys.__stdout__
    return buf.getvalue()[:-1]


__erase_lines = lambda count: sys.stdout.write((CURSOR_UP_ONE + ERASE_LINE) * count)


def menu_prompt(options):
    position = 0

    while True:

        buf = __print_menu(position, options)
        print buf

        v = f()
        if v == UP:
            position = max(0, position - 1)
        elif v == DOWN:
            position = min(position + 1, len(options) - 1)
        elif v[0] == '\n':
            return position

        __erase_lines(len(options))


if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit(1)
    # TODO: provide cli switch to make output be return code or stdout, as below
    print menu_prompt(sys.argv[1:])
