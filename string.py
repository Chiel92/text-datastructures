"""This module contains the trivial string datastructure."""
from text import Text


class String(Text):

    """Trivial text datastructure implemented by a single string."""

    def __init__(self, string):
        self.string = string

    def get(self, beg, end):
        """Lookup the text between beg and end."""
        return self.string[beg:end]

    def set(self, beg, end, string):
        """Replace the text between beg and end with string."""
        self.string = self.string[:beg] + string + self.string[end:]

