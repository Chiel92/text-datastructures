"""This module contains the rope datastructure."""
from text import Text


class Rope(Text):

    """Rope text data structure."""

    def __init__(self, string):
        self.root = RopeNode(None, None, None)

    def __getitem__(self, arg):
        """We don't support the step parameter of a slice object."""
        if isinstance(arg, int):
            index = arg
            length = 1
        else:
            if arg.step != None:
                raise Exception('We don\'t support the step parameter in slice objects.')
            index = arg.start
            length = arg.stop - arg.start

        strings = []
        while length > 0:
            string = self.lookup(self.root, index, length)
            assert string

            consumed_length = len(string)
            length -= consumed_length
            index += consumed_length
            strings.append(string)

        return ''.join(strings)

    def lookup(self, node, index, length):
        """Perform a recursive lookup query."""
        if isinstance(node, RopeLeaf):
            return node.string[index:index + length]
        else:
            if node.weight < index:
                return self.lookup(node.right, index - node.weight, length)
            else:
                return self.lookup(node.left, index, length)


class RopeNode:

    """A node in a rope."""

    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right
        self.weight = 0  # TODO


class RopeLeaf:

    """A leaf in a rope."""

    def __init__(self, parent, string):
        self.parent = parent
        self.string = string
        self.weight = len(string)
