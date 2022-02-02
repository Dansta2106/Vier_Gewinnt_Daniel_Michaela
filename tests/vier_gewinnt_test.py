import unittest

import vier_gewinnt
from vier_gewinnt import *


class VierGewinntTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.spieler = vier_gewinnt.spieler
        self.spielerAusgabetest = vier_gewinnt.Spieler.spielerAusgabe(self.spieler)
        self.spielerAusgabetest2 = vier_gewinnt.Spieler.spielerAusgabe()

    def test_SpielerAusgabe(self):
        self.assertEqual(self.spielerAusgabetest, "Spieler 1 ist dran")
        self.assertEqual(self.spielerAusgabetest2, "Spieler 2 ist dran")




if __name__ == '__main__':
    unittest.main()