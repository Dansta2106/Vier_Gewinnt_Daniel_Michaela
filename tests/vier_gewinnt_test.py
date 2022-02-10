import unittest

import vier_gewinnt_daniel_michaela.vier_gewinnt


class VierGewinntTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.spieler = vier_gewinnt_daniel_michaela.vier_gewinnt.spieler
        self.end = vier_gewinnt_daniel_michaela.vier_gewinnt.end

        self.zeile1 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile1
        self.zeile2 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile2
        self.zeile3 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile3
        self.zeile4 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile4
        self.zeile5 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile5
        self.zeile6 = vier_gewinnt_daniel_michaela.vier_gewinnt.zeile6
        self.spielfeld1 = vier_gewinnt_daniel_michaela.vier_gewinnt.spielfeld
        self.eingabe_start = str(1)
        self.falsche_eingabe = str(8)
        self.falsche_eingabe2 = str("hallo")
        self.fehler = vier_gewinnt_daniel_michaela.vier_gewinnt.fehler
        self.setSpielfeld1 = vier_gewinnt_daniel_michaela.vier_gewinnt.Spielfeld.setSpielfeld(self.spielfeld1, self.eingabe_start)
        self.setSpielfeld2 = vier_gewinnt_daniel_michaela.vier_gewinnt.Spielfeld.setSpielfeld(self.spielfeld1, self.eingabe_start)
        self.setSpielfeld3 = vier_gewinnt_daniel_michaela.vier_gewinnt.Spielfeld.setSpielfeld(self.spielfeld1, self.eingabe_start)
        self.setSpielfeld4 = vier_gewinnt_daniel_michaela.vier_gewinnt.Spielfeld.setSpielfeld(self.spielfeld1, self.eingabe_start)
        self.setSpielfeld5 = vier_gewinnt_daniel_michaela.vier_gewinnt.Spielfeld.setSpielfeld(self.spielfeld1, self.falsche_eingabe)
        self.gewinnVertikal = vier_gewinnt_daniel_michaela.vier_gewinnt.Gewinnabfrage.vertikaleAbfrage(self.spielfeld1)

        self.spielerAusgabetest = vier_gewinnt_daniel_michaela.vier_gewinnt.Spieler.spielerAusgabe(self.spieler)

    def test_SpielerAusgabe(self):
        self.assertEqual(self.spielerAusgabetest, "Spieler 1 ist dran")

    def test_setSpielfeld(self):
        self.assertEqual(self.spielfeld1[5][0], 1)
        self.assertEqual(self.spielfeld1[4][0], 1)
        self.assertEqual(self.spielfeld1[3][0], 1)
        self.assertEqual(self.spielfeld1[2][0], 1)
        self.assertTrue(self.fehler)

    def test_vertikaleAbfrage(self):
        self.assertTrue(self.end)




if __name__ == '__main__':
    unittest.main()
