"""This module contains an abstract class for text datastructures."""


class Text:

    """Abstract class for text data structures."""

    def __init__(self, string):
        raise Exception('An abstract method cannot be called.')

    def get(self, beg, end):
        """Lookup the text between beg and end."""
        raise Exception('An abstract method cannot be called.')

    def set(self, beg, end, string):
        """Replace the text between beg and end with string."""
        raise Exception('An abstract method cannot be called.')

    def __getitem__(self, arg):
        beg, end = convert_arg(arg)
        return self.get(beg, end)

    def __setitem__(self, arg, val):
        beg, end = convert_arg(arg)

        if not isinstance(val, str):
            raise Exception('Invalid val passed, not a string instance.')

        self.set(beg, end, val)


def convert_arg(arg):
    """We don't support the step parameter of a slice object."""
    if isinstance(arg, int):
        beg = arg
        end = arg + 1
    else:
        if arg.step != None:
            raise Exception('We don\'t support the step parameter in slice objects.')
        beg = arg.start
        end = arg.stop

    return beg, end
