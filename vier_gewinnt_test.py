import unittest
from vier_gewinnt import *


class VierGewinntTestCases(unittest.TestCase):

    def setUp(self):
        self.spielerWechsel = Spieler().spielerWechsel()
        self.spieler1 = spieler
        self.spieler2 = spieler

    def test_spielerWechsel(self):
        self.assertEqual(1, self.spielerWechsel(-1))







if __name__ == '__main__':
    unittest.main()
