"""
This is an example of a typical stack as a data structure in python.
"""
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2012, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "1.0.l"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Production"


class Stack():
    """ This is a class representing the typical Stack Data Structure """
    def __init__(self):
        self.nodes = []

    def push(self, element):
        """ Puts the element on the top of the stack """
        self.nodes.insert(0, element)

    def pop(self):
        """ Removes the top element from the stack """
        if self.len() is not None:
            self.nodes.pop(0)

    def len(self):
        """ Gets the length of the stack and returns "None" if empty """
        if len(self.nodes) == 0:
            return None
        else:
            return len(self.nodes)
