"""This module contains an abstract class for text datastructures."""


class Text:

    """Abstract class for text data structures."""

    def __init__(self, string):
        raise Exception('An abstract method cannot be called.')

    def __getitem__(self, index):
        raise Exception('An abstract method cannot be called.')

