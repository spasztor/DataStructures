"""
This is an example of a typical Queue as a data structure in Python.
"""
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "1.0.l"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Production"


class Queue():
    """ This is a class representing the typical Queue Data Structure """
    def __init__(self):
        self.nodes = []

    def push(self, element):
        """ Puts the element on the bottom of the Queue """
        self.nodes.insert(len(self.nodes), element)

    def pop(self):
        """ Removes the top element from the Queue """
        if self.len() is not None:
            self.nodes.pop(0)

    def len(self):
        """ Gets the length of the Queue and returns "None" if empty """
        if len(self.nodes) == 0:
            return None
        else:
            return len(self.nodes)
