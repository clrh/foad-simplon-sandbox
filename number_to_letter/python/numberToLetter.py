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
    def test_17_done_dixsept(self):
        self.assertEqual(numberToLetter(17), "dix-sept")
    def test_18_done_dixhuit(self):
        self.assertEqual(numberToLetter(18), "dix-huit")
    def test_19_done_dixneuf(self):
        self.assertEqual(numberToLetter(19), "dix-neuf")
    def test_23_done_vingttrois(self):
        self.assertEqual(numberToLetter(23), "vingt-trois")

def numberToLetter(number):
    values = {
            1:  "un",
            2:  "deux",
            3:  "trois",
            4:  "quatre",
            5:  "cinq",
            6:  "six",
            7:  "sept",
            8:  "huit",
            9:  "neuf",
            10: "dix",
            20: "vingt",
            }
    if number >= 17 and number <= 19:
        return values[10] + "-" + values[number - 10]
    if number > 20:
        return values[20] + "-" + values[number - 20]

    return values[number]

if __name__ == '__main__':
        unittest.main()
