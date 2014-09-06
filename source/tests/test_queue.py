"""
This is a unit test of the Queue class in 'Queue.py'.
"""
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL      "
__version__ = "1.0.l"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Production"

import os
import sys
import unittest

LibraryPath = os.path.abspath('../')
sys.path.insert(0, LibraryPath)
import Queue


class TestQueueMethods(unittest.TestCase):
    """ Tests the methods that can be used for the Queue Class in stack.py. """
    def setUp(self):
        """ Used for unittest initiation. """
        self.queue = Queue.Queue()

    def clearQueue(self):
        """ Clears the Queue for testing purposes. """
        self.queue.nodes = []

    def test_push(self):
        """ Tests queue.push(). """
        self.clearQueue()

        self.queue.push(1)
        self.queue.push(2)

        self.assertEquals(self.queue.nodes[0], 1)
        self.assertEquals(self.queue.nodes[1], 2)

    def test_pop(self):
        """ Tests queue.pop(). """
        self.clearQueue()

        self.queue.nodes.append(1)
        self.queue.nodes.append(2)
        self.queue.pop()

        self.assertEquals(len(self.queue.nodes), 1)

    def test_pop_when_empty(self):
        """ Tests queue.pop() when the queue is empty. """
        self.clearQueue()

        self.queue.pop()

        self.assertEquals(len(self.queue.nodes), 0)

    def test_len(self):
        """ Tests queue.len(). """
        self.clearQueue()

        self.queue.nodes.append(1)
        self.queue.nodes.append(2)

        self.assertEquals(self.queue.len(), 2)

    def test_len_when_empty(self):
        """ Tests queue.len() when the queue is empty. """
        self.clearQueue()

        self.assertEquals(self.queue.len(), None)

testSuite = unittest.TestLoader().loadTestsFromTestCase(TestQueueMethods)
unittest.TextTestRunner(verbosity=2).run(testSuite)
