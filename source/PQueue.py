"""
This is an example of a typical PQueue as a data structure in Python.
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


class PQueue():
    """
    This is a class representing the typical PQueue Data Structure.
    """
    def __init__(self):
        self._elements = []
        self._priority_map = []

    def len(self):
        """ Returns the length of the PQueue. """
        return len(self._elements)

    def push(self, priority, element):
        """
        Puts the element into the PQueue with a priority mapped to the
        index on the stack.
        """
        self._elements.append(element)
        self._priority_map.append(priority)

    def get_priorities(self):
        """
        Returns a list of priorities sorted by insertino order or None
        if the pqueue is empty.
        """
        returned_list = self._priority_map
        if self.len() is not 0:
            return returned_list
        else:
            return None

    def get_priority(self):
        """
        Finds the lowest priority element in the pqueue by looping
        though all elements in the pqueue. Returns none if pqueue is
        empty.
        """
        if self.len() is not 0:
            priorities = list(self.get_priorities())
            priorities.sort()

            priority = priorities.pop(0)

            index = self._priority_map.index(priority)
            return self._elements[index]
        else:
            return None

    def pop(self):
        """
        Removes the element with the lowest priority from the stack. If
        the element shares the priority with another then the order of
        insertion dictates how it will be removed on a first come first
        served basis.
        """

        if self.len() is not 0:
            index = self._elements.index(self.get_priority())
            self._elements.pop(index)
            self._priority_map.pop(index)
