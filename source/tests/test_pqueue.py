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
import pqueue


class TestPQueueMethods(unittest.TestCase):
    """ Tests the methods of PQueue in PQueue.py. """
    def setUp(self):
        """ Used for unittest initiation """
        self._pqueue = pqueue.PQueue()

    def _clean(self):
        """ Clears the PQueue for testing purposes """
        self._pqueue._queues = {}

    def test_len_with_one_push(self):
        """ Tests PQueue.len() with normal cond."""
        self._pqueue.push(1, "Foo")

        self.assertEquals(self._pqueue.len(), 1)

        self._clean()

    def test_len_with_several_push(self):
        """ Tests PQueue.len() with several pushes."""
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")
        self._pqueue.push(4, "Bar2")

        self.assertEquals(self._pqueue.len(), 3)

        self._clean()

    def test_len_with_push_and_pop(self):
        """ Tests PQueue.len() with pushes and pops."""
        self._pqueue.push(1, "Foo")
        self._pqueue.push(1, "Bar")
        self._pqueue.push(3, "Bar2")
        self._pqueue.pop()

        self.assertEquals(self._pqueue.len(), 2)

        self._clean()

    def test_pop(self):
        """ Tests PQueue.pop() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")

        self._pqueue.pop()

        self.assertEquals(self._pqueue.len(), 1)
        self.assertEquals(len(self._pqueue._queues.keys()), 1)
        self.assertEquals(self._pqueue._queues[4]._nodes[0], "Bar")

        self._clean()

    def test_pop_when_empty(self):
        """ Tests PQueue.pop() when the pqueue is empty """
        self._pqueue.pop()

        self.assertEquals(self._pqueue.len(), 0)
        self.assertEquals(len(self._pqueue._queues.keys()), 0)

        self._clean()

    def test_push(self):
        """ Tests PQueue.push() """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(4, "Bar")

        self.assertEquals(self._pqueue.len(), 2)
        self.assertEquals(len(self._pqueue._queues.keys()), 2)
        self.assertEquals(self._pqueue._queues[1]._nodes[0], "Foo")
        self.assertEquals(self._pqueue._queues[4]._nodes[0], "Bar")

        self._clean()

    def test_push_same_priorities(self):
        """ Tests PQueue.push() with same priorities """
        self._pqueue.push(1, "Foo")
        self._pqueue.push(1, "Bar")

        self.assertEquals(self._pqueue.len(), 2)
        self.assertEquals(len(self._pqueue._queues.keys()), 1)
        self.assertEquals(self._pqueue._queues[1]._nodes[0], "Foo")
        self.assertEquals(self._pqueue._queues[1]._nodes[1], "Bar")

        self._clean()

_TEST_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestPQueueMethods)
unittest.TextTestRunner(verbosity=2).run(_TEST_SUITE)
