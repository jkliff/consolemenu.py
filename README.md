Command line menu prompt.
Produces a multi-option prompt with selection possible through keyboard UP and DOWN strokes.

- The function menu_prompt returns the index of the selected option.
- If called as a script, prints to stdout the option (useful to build interactive shells scripts from languages othar
than Python).

Example as shell utility:
$ python -m consolemenu "asdf" "qwer" "foo" "bar bababa?"

Install with
$ sudo python setup.py install