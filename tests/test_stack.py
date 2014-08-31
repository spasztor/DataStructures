#!/usr/bin/env python

import os, sys, unittest

lib_path = os.path.abspath('../')
sys.path.insert(0, lib_path)

import stack

class test_stack(unittest.TestCase):
	
	def setup(self):
		self.stack = stack.stack()

	def test_push(self):
		self.stack.push(1)
		self.stack.push(2)

		self.assertEquals(self.stack.node[0].value, 2)
		self.assertEquals(self.stack.node[1].value, 1)
