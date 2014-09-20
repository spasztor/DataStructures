"""
This is an example of a typical Queue as a data structure in Python.
"""
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Production"


class Queue():
    """ This is a class representing the typical Queue Data Structure """
    def __init__(self):
        self._nodes = []

    def push(self, element):
        """ Puts the element on the bottom of the Queue """
        self._nodes.insert(len(self._nodes), element)

    def pop(self):
        """ Removes the top element from the Queue """
        if self.len() is not 0:
            return self._nodes.pop(0)
        else:
            return None

    def len(self):
        """ Gets the length of the Queue. """
        return len(self._nodes)
