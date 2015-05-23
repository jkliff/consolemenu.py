consolemenu.py
==============


Command line menu prompt.

Produces a multi-option prompt with selection possible through keyboard UP and DOWN strokes.

- The function menu_prompt returns the index of the selected option.
- If called as a script, prints to stdout the option (useful to build interactive shells scripts from languages other
than Python).

Example as shell utility:
```
$ python -m consolemenu "option 1" "option 2" "option 3" 
```

Example from python script:

    
    >>> import consolemenu
    >>> consolemenu.menu_prompt(['option 1', 'option 2', 'option 3'])

Examples above produce an interactive menu as follows:

    >>  option 1
        option 2
        option 3

Install with
```
$ sudo python setup.py install
```

TODO:

- Does not support proper coloring (as in with use of colored or termcolor) in the menu items.
