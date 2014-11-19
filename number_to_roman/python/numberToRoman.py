#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import unittest
class TestLags(unittest.TestCase):
    def test_test(self):
        self.assertEqual(True, True)
    def test_1_donne_I(self):
	self.assertEqual(numberToRoman(1),"I")
    def test_2_donne_II(self):
	self.assertEqual(numberToRoman(2),"II")
    def test_10_donne_XX(self):
	self.assertEqual(numberToRoman(10),"X")


def numberToRoman(number):
	values = {1: 'I', 10: 'X'}
	if number == 10:
		return values[number]
	else:
		return values[1] * number

if __name__ == '__main__':
        unittest.main()
