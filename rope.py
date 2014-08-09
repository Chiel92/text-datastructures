"""This module contains the rope datastructure."""
from text import Text


class Rope(Text):

    """A Rope is a recursive text data structure."""

    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right
        self.lenght = 0 # TODO

    def get(self, beg, end):
        """Lookup the text between beg and end."""
        assert 0 <= beg <= end <= self.weight

        index = beg
        length = end - beg

        # Lookup all relevant leaves and concatenate the requested part
        strings = []
        while length > 0:
            string = get_leaf(self, index, length)
            assert string

            consumed_length = len(string)
            length -= consumed_length
            index += consumed_length
            strings.append(string)
        return ''.join(strings)

    def set(self, beg, end, string):
        """Replace the text between beg and end with given string."""
        assert 0 <= beg <= end <= self.weight

        # Split at beg and end
        left_rope, rest = split(self, beg)
        _, right_rope = split(rest, end - beg)

        # Concat left and right part with new string
        inserted_rope = build_rope(string)
        new_rope = concat(concat(left_rope, inserted_rope), right_rope)

        # Rebalance the resulting rope
        new_rope.balance()
        return new_rope

    def balance(self):
        """Rebalance the rope structure."""
        pass

    @property
    def weight(self):
        return self.left.length


def build_rope(string):
    """Build a rope for the given string."""
    return NotImplemented

def get_leaf(node, index, length):
    """Perform a recursive lookup query."""
    if isinstance(node, RopeLeaf):
        return node.string[index:index + length]
    else:
        if node.weight < index:
            return get_leaf(node.right, index - node.weight, length)
        else:
            return get_leaf(node.left, index, length)


def concat(left_rope, right_rope):
    """Concatenate two ropes."""
    root = Rope(None, left_rope, right_rope)
    left_rope.parent = root
    right_rope.parent = root
    return root


def split(rope, index):
    """Split a rope into two ropes at given index."""
    if isinstance(rope, RopeLeaf):
        left_string = rope.string[:index]
        right_string = rope.string[index:]
        return RopeLeaf(None, left_string), RopeLeaf(None, right_string)
    else:
        pass


class RopeLeaf:

    """A leaf in a rope."""

    def __init__(self, parent, string):
        self.parent = parent
        self.string = string

    @property
    def weight(self):
        return len(self.string)
