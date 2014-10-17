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

import queue

class PQueue():
    """
    This is a class representing the typical PQueue Data Structure.
    """
    def __init__(self):
        self._queues = {}

    def len(self):
        """ Returns the length of the PQueue. """
        size = 0
        for key in self._queues:
            size += self._queues[key].len()

        return size

    def push(self, priority, element):
        """
        Put the element into the PQueue with a priority mapped to the
        index on the queue.
        """
        if priority in self._queues:
            self._queues[priority].push(element)
        else:
            new_queue = queue.Queue()
            new_queue.push(element)
            self._queues[priority] = new_queue

    def pop(self):
        """
        Removes the element with the lowest priority from the stack. If
        the element shares the priority with another then the order of
        insertion dictates how it will be removed on a first come first
        served basis.
        """
        if self.len() is not 0:
            priorities = sorted(self._queues.keys())
            priority_element = priorities[0]
            self._queues[priority_element].pop()
            if self._queues[priority_element].len() is 0:
                del self._queues[priority_element]
