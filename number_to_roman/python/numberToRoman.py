#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import unittest
class TestLags(unittest.TestCase):
    def test_test(self):
        self.assertEqual(True, True)
    def test_1_donne_I(self):
	self.assertEqual(numberToRoman(1),"I")

def numberToRoman(number):
	if number == 1:
		return "I"

if __name__ == '__main__':
        unittest.main()
