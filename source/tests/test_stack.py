"""
This is a unit test of the stack class in 'stack.py'.
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

import os
import sys
import unittest

stackLibraryPath = os.path.abspath('../')
sys.path.insert(0, stackLibraryPath)
import stack


class TestStackMethods(unittest.TestCase):
    """ Tests the methods that can be used for the Stack Class in stack.py. """
    def setUp(self):
        """ Used for unittest initiation. """
        self.stack = stack.Stack()

    def clearStack(self):
        """ Clears the stack for testing purposes. """
        self.stack.nodes = []

    def test_push(self):
        """ Tests stack.push(). """
        self.clearStack()

        self.stack.push(1)
        self.stack.push(2)

        self.assertEquals(self.stack.nodes[0], 2)
        self.assertEquals(self.stack.nodes[1], 1)

    def test_pop(self):
        """ Tests stack.pop(). """
        self.clearStack()

        self.stack.nodes.append(1)
        self.stack.nodes.append(2)

        self.assertEquals(self.stack.pop(), 1)
        self.assertEquals(len(self.stack.nodes), 1)

    def test_pop_when_empty(self):
        """ Tests stack.pop() when the stack is empty. """
        self.clearStack()

        self.stack.pop()

        self.assertEquals(len(self.stack.nodes), 0)

    def test_len(self):
        """ Tests stack.len(). """
        self.clearStack()

        self.stack.nodes.append(1)
        self.stack.nodes.append(2)

        self.assertEquals(self.stack.len(), 2)

    def test_len_when_empty(self):
        """ Tests stack.len() when the stack is empty. """
        self.clearStack()

        self.assertEquals(self.stack.len(), None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStackMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
