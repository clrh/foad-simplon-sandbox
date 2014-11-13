#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Consigne
# Je possède un avion que je loue
# Je le loue que s'il m'est rendu
# 3 données: départ, durée, profit
# Le programme sélectionne automatiquement les demandes de vol pour faire un maximum de profit

import unittest
class TestLags(unittest.TestCase):
    def test_test(self):
        self.assertEqual(True, True)
    def test_no_demand(self):
        demandes = []
	self.assertEqual(0,lags(demandes))
    def test_uniq_demand(self):
        demandes = [[2,4,9]]
        self.assertEqual(9,lags(demandes))

def lags(demandes):
    print len(demandes)
    if len(demandes) == 0:
        return 0
    else:
        return demandes[0][2]
    return len(demandes)

if __name__ == '__main__':
        unittest.main()






