#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import unittest
class TestLags(unittest.TestCase):
    def test_test(self):
        self.assertEqual(True, True)
    def test_1_done_un(self):
        self.assertEqual(numberToLetter(1), "un")
    def test_2_done_deux(self):
        self.assertEqual(numberToLetter(2), "deux")

def numberToLetter(number):
    values = {1: "un",
            2: "deux",
            }
    return values[number]

if __name__ == '__main__':
        unittest.main()
