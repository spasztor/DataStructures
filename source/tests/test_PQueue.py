""" This is a unit test of the PQueue class in 'Queue.py'."""
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "1.0.l"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Production"

import os
import sys
import unittest

_LIBRARY_PATH = os.path.abspath('../')
sys.path.insert(0, _LIBRARY_PATH)
import PQueue


class TestPQueueMethods(unittest.TestCase):
    """ Tests the methods of PQueue in PQueue.py. """
    def setUp(self):
        """ Used for unittest initiation """
        self._pqueue = PQueue.PQueue()

    def _clean(self):
        """ Clears the PQueue for testing purposes """
        self._pqueue._elements = []
        self._pqueue._priority_map = []

    def test_len(self):
        """ Tests PQueue.len() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")

        self.assertEquals(self._pqueue.len(), 2)

        self._clean()

    def test_pop(self):
        """ Tests PQueue.pop() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")
        self._pqueue.pop()

        self.assertEquals(self._pqueue.len(), 1)
        self.assertEquals(self._pqueue._elements[0], "Bar")
        self.assertEquals(self._pqueue._priority_map[0], 4)

        self._clean()

    def test_pop_when_empty(self):
        """ Tests PQueue.pop() when the pqueue is empty """
        self._pqueue.pop()

        self.assertEquals(self._pqueue.len(), 0)

        self._clean()

    def test_push(self):
        """ Tests PQueue.push() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")

        self.assertEquals(self._pqueue._elements[0], "Foo")
        self.assertEquals(self._pqueue._elements[1], "Bar")
        self.assertEquals(self._pqueue._priority_map[0], 1)
        self.assertEquals(self._pqueue._priority_map[1], 4)

        self._clean()

    def test_push_same_priorities(self):
        """ Tests PQueue.push() with same priorities """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(1, "Bar")

        self.assertEquals(self._pqueue._elements[0], "Foo")
        self.assertEquals(self._pqueue._elements[1], "Bar")
        self.assertEquals(self._pqueue._priority_map[0], 1)
        self.assertEquals(self._pqueue._priority_map[1], 1)

        self._clean()

    def test_get_priorities(self):
        """ Tests PQueue.get_priorities() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")

        self.assertEquals(self._pqueue.get_priorities(), [1, 4])

        self._clean()

    def test_get_priority(self):
        """ Tests Pqueue.get_priority() """
        self._pqueue.push(4, "Bar")
        self._pqueue.push(1, "Foo")

        self.assertEquals(self._pqueue.get_priority(), "Foo")

        self._clean()

    def test_get_priority_when_same(self):
        """ Tests PQueue.get_priority() when priorities are the same """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(1, "Bar")

        self.assertEquals(self._pqueue.get_priority(), "Foo")

        self._clean()

_TEST_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestPQueueMethods)
unittest.TextTestRunner(verbosity=1).run(_TEST_SUITE)
